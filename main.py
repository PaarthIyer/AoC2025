import argparse
import importlib
from utils.utils import timer, handle_input


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AoC 2025 - day and problem are required. Input can either be piped or one of -i/-t can be used."
    )
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("-p", "--problem", type=int, required=True)
    parser.add_argument(
        "-s",
        "--suffix",
        type=str,
        help="Runs problemX_(suffix).py from the given day",
        default="",
    )
    parser.add_argument(
        "-i",
        "--input",
        action="store_true",
        help="Uses dayX/input.in as the input",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Uses dayX/test.in as the input",
    )
    args = parser.parse_args()

    # Input handling
    if args.input and args.test:
        parser.error("Only one of -i or -t can be used, not both")

    path = "input file"
    if args.input:
        path = f"day{args.day}/input.in"
    elif args.test:
        path = f"day{args.day}/test.in"

    data = handle_input(path)

    # Function loading
    suffix = f"_{args.suffix}" if args.suffix != "" else ""

    fn = importlib.import_module(f"day{args.day}.problem{args.problem}{suffix}").main
    fn = timer(fn)

    # Execution
    fn(data)


if __name__ == "__main__":
    main()
