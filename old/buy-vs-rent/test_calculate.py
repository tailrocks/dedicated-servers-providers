"""Numerical model checks only: no CPU, storage or CI performance tests.

Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
"""

from decimal import Decimal as D
import unittest

import calculate as c


class FinancialModelTests(unittest.TestCase):
    def test_break_even_agrees_with_exhaustive_month_search(self):
        # An independent month-by-month oracle checks crossings, exact equality,
        # sunk/no setup, zero operating costs, and no crossing over this grid.
        for hardware in (0, 1, 900, 1000, 1001):
            for setup in (0, 1, 300, 1200):
                for rent in (0, 100, 200):
                    for running in (0, 90, 100, 210):
                        expected = next((m for m in range(2000)
                                         if hardware + m * running <= setup + m * rent), None)
                        self.assertEqual(c.break_even(hardware, setup, rent, running), expected)

    def test_fractional_crossing_rounds_up_without_rounding_money_inputs(self):
        self.assertEqual(c.break_even("1000.00001", 0, 100, 0), 11)
        self.assertEqual(c.break_even(1000, 0, 100, 0), 10)
        self.assertEqual(c.money("1.005"), "1.01")

    def test_electricity_uses_wall_watts_and_730_hours(self):
        self.assertEqual(c.electricity(275, 730, "0.3116"), D("62.5537"))
        self.assertEqual(c.electricity(0, 730, "0.3116"), D("0"))

    def test_fx_cross_rate_and_round_trip(self):
        rates = {"EUR": 1, "SGD": "1.4176", "MYR": "4.5205", "USD": "1.0992"}
        self.assertEqual(c.convert(100, "EUR", "SGD", rates), D("141.7600"))
        self.assertAlmostEqual(c.convert(c.convert(19153, "MYR", "SGD", rates),
                                        "SGD", "MYR", rates), D("19153"), places=20)

    def test_four_scenarios_keep_electricity_and_internet_independent(self):
        expected = [D("1000"), D("1120"), D("1240"), D("1360")]
        actual = [c.buy_cost(1000, 12, 10 if e else 0, 20 if i else 0)
                  for e, i in c.SCENARIOS.values()]
        self.assertEqual(actual, expected)
        self.assertEqual(c.buy_cost(1000, 12, 10, 20, 5, 50), D("1470"))

    def test_setup_and_maintenance_change_crossing(self):
        self.assertEqual(c.break_even(1000, 100, 100, 10), 10)
        self.assertEqual(c.break_even(1000, 0, 100, 10), 12)
        self.assertIsNone(c.break_even(1000, 0, 100, 100))
        self.assertIsNone(c.break_even(1000, 0, 100, 101))

    def test_annual_prepayment_is_not_a_monthly_invoice(self):
        self.assertEqual(c.prepaid_rent_cost(0, "301.5", 6, 12), D("3618"))
        self.assertEqual(c.prepaid_rent_cost(0, "301.5", 12, 12), D("3618"))
        self.assertEqual(c.prepaid_rent_cost(0, "301.5", 13, 12), D("7236"))
        self.assertEqual(c.prepaid_rent_cost(50, "301.5", 0, 12), D("50"))

    def test_internet_promotion_and_after_term_rate(self):
        plan = {"monthly": "27.99", "first_month": "7.99", "after_term_monthly": 30,
                "term_months": 24, "setup": 0}
        self.assertEqual(c.internet_cost(plan, 0), D("0"))
        self.assertEqual(c.internet_cost(plan, 1), D("7.99"))
        self.assertEqual(c.internet_cost(plan, 24), D("651.76"))
        self.assertEqual(c.internet_cost(plan, 36), D("1011.76"))

    def test_known_customer_tax_is_applied_once(self):
        rates = {"EUR": 1, "SGD": "1.4176"}
        rental = {"id": "ax162_1", "monthly": 614, "setup": 304,
                  "currency": "EUR", "native_tax_basis": "Before tax"}
        sg = c.rental_terms(rental, "SG", rates)
        my = c.rental_terms(rental, "MY", rates)
        self.assertEqual(sg[0], D("948.742976"))
        self.assertEqual(my[0], D("870.4064"))
        rental.update(id="observed_local_tax", comparison_tax_percent=11)
        self.assertEqual(c.rental_terms(rental, "MY", rates)[0], D("966.151104"))

    def test_pool_scaling_is_explicit(self):
        build = {"compiler_proxy": {"candidate_work_rate": 250, "baseline_work_rate": 400,
                                     "node_count": 2, "pool_efficiency": "0.8"}}
        self.assertEqual(c.benchmark_ratio(build), D("1.00"))
        self.assertIsNone(c.benchmark_ratio({}))


if __name__ == "__main__":
    unittest.main()
