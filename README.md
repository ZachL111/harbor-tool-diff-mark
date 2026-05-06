# harbor-tool-diff-mark

`harbor-tool-diff-mark` is a compact Python repository for cli tools, centered on this goal: Package a Python local lab for diff analysis with windowed input fixtures, late-data behavior checks, and documented operating limits.

## Purpose

The project exists to keep a narrow engineering decision visible and testable. For this repo, that decision is how file span and argument risk should influence a review result.

## Harbor Tool Diff Mark Review Notes

Start with `report density` and `file span`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## What Is Covered

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/harbor-tool-diff-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `report density` and `file span`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Implementation Notes

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The added Python path is deliberately direct, with fixtures doing most of the explaining.

## Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Audit Path

The same command runs the local verification path. The highest-scoring domain case is `recovery` at 242, which lands in `ship`. The most cautious case is `baseline` at 158, which lands in `ship`.

## Limits

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.
