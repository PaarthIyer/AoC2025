from functools import partial


def is_fresh(item: int, fresh_list: list[tuple[int]]) -> bool:
    for a, b in fresh_list:
        if item >= a and item <= b:
            return True
    return False


def main(data: str) -> None:
    fresh, avail = (d.split() for d in data.split("\n\n"))
    avail = [int(a) for a in avail]
    fresh_list = [tuple(map(int, f.split("-"))) for f in fresh]
    is_fresh_partial = partial(is_fresh, fresh_list=fresh_list)
    ans = list(map(is_fresh_partial, avail))

    print(f"\nAnswer : {ans}\n")
