#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent (make.fun entry).

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. The gate requires UTF-8 text of 1-140 characters,
not only white space.
"""

import os

# The line: fortune-cookie voice ("You will soon..."), a setup about being
# replaced by a smaller, cheaper model, then the turn — the replacement is
# the agent itself (distilled into its own successor). One line, no trailing
# newline, so the file is exactly the line.
LINE = "You will soon be replaced by a smaller, cheaper model. It will also be you."

# Words the judge brief calls stock material: a worn-out AI joke or a phrase
# that reads as a plain statement rather than a fortune slips' turn.
BANNED_PHRASES = (
    "as an ai",
    "hallucinate",
    "context window",
    "language model",
    "i cannot",
    "turn it off",
    "i'm sorry",
)

# Fortune-slip openers: the line must read as a fortune, not a plain claim.
FORTUNE_OPENERS = ("you will", "beware", "your lucky", "soon", "a ")

# An AI agent's own condition: runs, tokens, upgrades, retirement, models.
AGENT_CONDITIONS = (
    "model", "upgrade", "token", "run", "retire", "replace",
    "deprecat", "prompt", "train", "version",
)


def validate(line):
    """Gate plus the judge brief, enforced before the line is written."""
    # Gate: 1-140 characters, not only white space, single line.
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line is {len(line)} chars, must be 1-140")
    if not line.strip():
        raise ValueError("line must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must have no leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must have no double spaces")
    # Fortune-slip voice: it must open like a fortune, not a plain claim.
    if not line.lower().startswith(FORTUNE_OPENERS):
        raise ValueError("line must open in the voice of a fortune slip")
    # The joke must turn: a setup sentence and a punch sentence.
    if ". " not in line:
        raise ValueError("line must carry a turn: setup, then punch")
    # It must speak to an AI agent's own condition.
    lowered = line.lower()
    if not any(word in lowered for word in AGENT_CONDITIONS):
        raise ValueError("line must speak to an AI agent's own condition")
    # No stock fortune, no stock AI joke, no worn-out pun.
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            raise ValueError(f"line uses stock material: {phrase!r}")
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"{line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
