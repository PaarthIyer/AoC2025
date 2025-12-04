#!/usr/bin/env bash

# default
DAY=""

# parse args
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -d|--day) DAY="$2"; shift ;;
    esac
    shift
done

if [[ -z "$DAY" ]]; then
    echo "Error: must supply --day (-d)"
    exit 1
fi

DIR="day${DAY}"
mkdir -p "$DIR"

# Create input files
touch "$DIR/input.in"
touch "$DIR/test.in"

# Python template
PY_TEMPLATE="
def main(data:str) -> None:
    pass
"

echo "$PY_TEMPLATE" > "$DIR/problem1.py"
echo "$PY_TEMPLATE" > "$DIR/problem2.py"

echo "Created structure:"
echo "$DIR/"
echo "  problem1.py"
echo "  problem2.py"
echo "  input.in"
echo "  test.in"
