# Harbor Tool Diff Mark Walkthrough

This note is the quickest way to read the extra review model in `harbor-tool-diff-mark`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 158 | ship |
| stress | terminal width | 174 | ship |
| edge | argument risk | 189 | ship |
| recovery | report density | 242 | ship |
| stale | file span | 183 | ship |

Start with `recovery` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

If `baseline` becomes less cautious without a clear reason, I would inspect the drag input first.
