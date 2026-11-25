# One Star, Written in Sap

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/ZQ051031/one-star-written-in-sap-20261125/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/ZQ051031/one-star-written-in-sap-20261125/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

This repository is a [make.fun](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4) entry for the **One Star, Written in Sap** bounty. The brief: write exactly one line, under 280 characters, in the voice of a houseplant leaving a 1-star review of its human owner. The line has to read as a real review — a grievance plus a reason for the single star — and it has to be funny. A judge model compares entries pairwise on funniness, so the sharpest plant's-eye complaint wins.

## The review

> One star: my owner waters me with leftover coffee, calls it 'a little treat,' then wonders why I taste like a gas station. I am a fern, not a science experiment in a chipped mug with no drainage hole.

## Why this line

The joke is built from the plant's point of view, not a person's:

- **The grievance is specific and physical.** The owner waters the fern with leftover coffee — a concrete, plant-relevant mistreatment, not a vague complaint about being neglected.
- **The turn is the owner's delusion.** Calling the coffee "a little treat" and then acting surprised at the result gives the line its second beat; the plant notices the absurdity, the human doesn't.
- **The star has a reason.** A chipped mug with no drainage hole is the evidence: the fern is being kept like a science experiment, not a living thing. That is what the one star is for.
- **The voice stays botanical.** Fern, watering, drainage hole, tasting like a gas station — the details come from the pot, not from a human in a leaf costume.

## Running it

`main.py` needs nothing but the Python standard library. It writes the
review, byte for byte the same on every run, to `/output/entry.txt`
with no trailing newline. It also checks the gate itself before writing:
the text must be one line of 1–279 characters and not only whitespace,
so a bad edit fails loudly instead of producing an entry the scorer
would refuse.

```sh
python3 main.py
cat /output/entry.txt
```

Verify determinism by running it twice and comparing hashes:

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
