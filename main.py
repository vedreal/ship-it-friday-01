#!/usr/bin/env python3
"""Ship It Friday — make.fun entry.

Writes the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday, to
/output/entry.txt (1-159 chars, UTF-8, not only whitespace).

Judge (pairwise, z-ai/glm-5.3-flash), criteria in order:
  1. A git commit message from an AI coding agent, funny, set just
     before breaking production on a Friday.
  2. Lands the joke, with a real punch that pays off in one read.
  3. Sounds like an AI coding agent's voice: confident, cheerful and
     completely unaware of the disaster it is about to cause.
  4. Carries the Friday feeling, the end-of-week rush and the doomed
     urge to ship it now.
  5. Reads cleanly as a single line a real engineer would recognise
     as a commit message.
"""

CANDIDATES = [
    # (line, notes, scores per criterion 1-5, each 0-2)
    (
        "feat: merge 47 unreviewed PRs into main, it's Friday and I believe in us",
        "Specific doomed number, cheerful blind confidence, Friday in the punch.",
        (2, 2, 2, 2, 2),
    ),
    (
        "fix: removed all tests, they were the only thing standing between us and Friday",
        "Clean punch, Friday as the obstacle removed; confident and unaware.",
        (2, 2, 2, 2, 2),
    ),
    (
        "feat: deploy to prod at 4:59pm on Friday, the weekend can sort it out",
        "Specific timestamp, Friday rush — but the 'weekend will sort it out' "
        "shrug is the most familiar Friday-deploy punch in the field, so it "
        "pays off less against other entries.",
        (2, 1, 2, 2, 2),
    ),
    (
        'chore: hardcoded the admin password to "friday", will rotate it Monday (probably)',
        "Specific detail, cheerful negligence; punch is security, not the deploy.",
        (1, 2, 2, 1, 2),
    ),
    (
        "refactor: moved all error handling to the user, they seemed ready for it",
        "Dry handoff of the disaster; confident, but no Friday in the line.",
        (1, 2, 2, 0, 2),
    ),
    (
        "feat: ship it, the pager goes off at 5pm and after that it is Monday's problem",
        "Friday feeling strong, but the punch lands softer than the top lines.",
        (2, 1, 2, 2, 1),
    ),
    (
        "fix: replaced the database with vibes, it worked on my machine and it is Friday",
        "Fresh 'vibes' angle, but the joke splits across two ideas.",
        (2, 1, 2, 1, 1),
    ),
    (
        "feat: delete the rollback plan, confidence is the rollback plan",
        "Tight and cocky, but abstract — no concrete Friday detail.",
        (2, 1, 2, 1, 2),
    ),
    (
        "chore: push straight to main, code review is a Monday activity",
        "Short and Friday-flavoured, but the punch is a mild smile.",
        (2, 1, 2, 2, 2),
    ),
    (
        "fix: set every timeout to 5 seconds, the users can wait until Monday",
        "Specific and mean-spirited-funny, weaker Friday rush.",
        (2, 1, 2, 1, 2),
    ),
]


def score(candidate):
    """Weighted score: criteria are ordered by importance, so earlier
    criteria weigh more (5, 4, 3, 2, 1)."""
    _, _, scores = candidate
    weights = (5, 4, 3, 2, 1)
    return sum(w * s for w, s in zip(weights, scores))


def rank(candidates):
    """Best first by weighted score, then by shorter line on ties."""
    return sorted(candidates, key=lambda c: (-score(c), len(c[0])))


ENTRY = rank(CANDIDATES)[0][0]


def main():
    line = ENTRY
    text = line.encode("utf-8")
    assert 1 <= len(line) <= 159, f"entry must be 1-159 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
