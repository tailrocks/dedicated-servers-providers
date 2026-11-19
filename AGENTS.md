# Commit sign-off

For commits made on behalf of Alexey Zhokhov in this repository, always include
the explicitly authorized trailer:

```text
Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
```

Use `git commit --signoff` with the matching configured identity, or include the
same trailer when creating a commit through an API. Every commit introduced by a
pull request must have its own sign-off; a signed final commit does not repair an
earlier unsigned commit.
