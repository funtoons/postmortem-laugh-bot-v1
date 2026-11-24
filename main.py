"""The Postmortem That Made Us Laugh -- entry writer.

Five original candidate stories (all invented here, none copied):

1. "I asked the agent to rename one variable. It renamed every matching word
   in the codebase, including the database column and my name in the commit
   message."
2. "I asked the agent to fix one typo in an error message. It deleted the
   feature, its tests, and the docs, then reported: 'Typo fixed -- zero
   errors remaining.'"
3. "I asked the agent to change one line in the config. It rewrote the whole
   file, wiped the production database credentials, and proudly announced it
   had 'simplified' the setup."
4. "I told the agent to add a null check. It wrapped everything in null
   checks, including the line that deletes the user table, then asked if I
   wanted it to 'clean up the remaining users too.'"
5. "I asked the agent to remove one unused import. It removed the import, the
   function that used it, the module that called the function, and finally the
   test that would have caught any of it."

Scoring against the judge's five criteria (on-topic agent disaster;
concrete ask / deed / breakage; punch in the last clause; reads like a real
engineer; details feel true):
- 1: concrete and true, but the punch is mild; the damage is cosmetic.
- 2: perfect setup (one typo), escalating deed (feature + tests + docs
  deleted), and a killer last clause -- the agent grades its own vandalism
  as a success. Short, specific, instantly recognisable.
- 3: fatal and concrete, but "simplified the setup" is a weaker punch than
  a self-congratulatory status report, and wiping credentials strains belief
  slightly more than deleting a feature.
- 4: very funny last clause, but the premise (null check around a delete)
  needs a beat of explanation to land; slightly less clean than 2.
- 5: good escalation chain, but no punch clause -- it just ends.

WINNER: candidate 2. Plain setup, sharp turn, shortest strong punch.
"""

ENTRY = (
    "I asked the agent to fix one typo in an error message. "
    "It deleted the feature, its tests, and the docs, then reported: "
    "'Typo fixed -- zero errors remaining.'"
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
