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

## Complete repository changes

Alexey Zhokhov has explicitly requested that pull requests created or modified
for his repository tasks be committed, pushed and merged. Complete that workflow
after addressing review findings and passing the repository's required checks;
do not stop at a draft or ask again for permission already granted. Integrate
newer base-branch changes when needed and preserve other contributors' work.
Include the same sign-off on any authored integration or final merge commit.
