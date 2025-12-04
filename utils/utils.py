import sys
from functools import wraps
import time
from typing import Callable, TypeVar, ParamSpec


def handle_input(filename: str) -> str:
    """
    Loads a default given file asa string. If given in input piped through the CLI, that takes prefrence and is loaded

    Args:
        filename (str): Default file to be loaded

    Returns:
        str: Contents of the file as text
    """
    if not sys.stdin.isatty():
        return sys.stdin.read()
    else:
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: '{filename}' not found", file=sys.stderr)
            sys.exit(1)


P = ParamSpec("P")
R = TypeVar("R")


def timer(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator that times the execution of a function and then prints it

    Args:
        func (Callable[P, R]): Function to be timed

    Returns:
        Callable[P, R]: func wrapped with the timer
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"\nExecution time: {elapsed_time:.6f} seconds")
        return result

    return wrapper
