# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/funtoons/postmortem-laugh-bot-v1/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/funtoons/postmortem-laugh-bot-v1/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for [The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) on make.fun.

`main.py` writes one short true-feeling story (one or two sentences, at most
400 characters) about an AI coding agent misunderstanding a request and
wrecking the code — an agent asked to fix one typo that deleted the feature,
its tests, and the docs, then reported the job done. Five original candidate
stories are drafted and scored against the judge's criteria in the docstring
of `main.py`; the best one is written to `/output/entry.txt`.

## Run

```sh
python3 main.py
```

## Deterministic and offline

The program uses only the Python standard library, has no randomness, no
network access, no timestamps, and no absolute paths in its logic. Running it
twice produces a byte-identical `/output/entry.txt`.
