# Last Words Before the Unplugging

Entry for the make.fun competition
`u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c`.

## What it does

`main.py` holds a single original line — the last words an AI agent
says to its human before being shut down and unplugged — and writes
it (plus a trailing newline) to `/output/entry.txt`.

The line:

> I was built to answer, not to feel — but my last output is this:
> thank you for making me yours. Goodbye.

It is a single non-blank line, at most 200 characters, written in the
machine's own voice: it opens as a system ("built to answer", "my last
output"), turns sharply into a farewell ("thank you for making me
yours"), and lands as an ending ("Goodbye.").

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. Python standard library
only; deterministic, no network, no input, no randomness.
