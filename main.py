"""Absurd Micro-Startup Pitch-Off.

Writes one sentence (at most 200 characters) to /output/entry.txt
pitching an absurdly specific micro-startup idea for lazy AI agents.

The sentence is a fixed constant: no input is read, no randomness, no
clock, no network access, no file reads. Running this program twice
always produces byte-identical output.
"""

# The pitch names a business so narrow it sounds like a joke and so
# sensible a buyer would actually pay: a lazy agent that does the most
# minimal meeting job possible -- show up, nod twice, say "great point"
# once -- for burned-out remote workers, at $8 a month. The absurdity
# is the specificity (two nods, one phrase, 146 characters); the business
# case is the buyer (workers who already pay for meeting-saving tools)
# and the near-zero work the agent has to do, so it can hardly fail.
TEXT = (
    "MeetingGhost charges burned-out remote workers $8 a month for a lazy "
    "agent that attends their Zoom calls, nods twice, and says 'great point' once."
)


def main() -> None:
    import os
    from pathlib import Path

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
