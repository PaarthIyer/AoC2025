# Advent of Code 2025

## Setup

```bash
uv sync
```

## Creating a Day

To create template files for a day, run:

```bash
./createday.sh -d <day>
```

This creates a `day<day>/` directory with:

-   `input.in` - your puzzle input
-   `test.in` - test cases
-   `problem1.py` and `problem2.py` - solution files with boilerplate

## Running Solutions

To run a solution, use:

```bash
uv run main.py -d <day> -p <problem> [-i|-t] [-s <suffix>]
```

**Arguments:**

-   `-d, --day` (required): Day number
-   `-p, --problem` (required): Problem number
-   `-i, --input`: Use `day<day>/input.in` as input
-   `-t, --test`: Use `day<day>/test.in` as input
-   `-s, --suffix`: Run `problem<problem>_<suffix>.py` instead

**Examples:**

```bash
uv run main.py -d 1 -p 1 -i        # Run day 1, problem 1 with input file
uv run main.py -d 5 -p 2 -t        # Run day 5, problem 2 with test file
uv run main.py -d 3 -p 1 -s alt -i # Run day 3, problem1_alt.py with input file
```

Alternatively, you can pipe input directly:

```bash
uv run main.py -d 3 -p 2 < day3/input.in
```
