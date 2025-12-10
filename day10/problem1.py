from collections import deque


def parse_row(row: str) -> tuple[int, list[tuple[int, ...]]]:
    parts = row.split(" ")
    final_state = int(parts[0][1:-1].replace(".", "0").replace("#", "1")[::-1], 2)
    switch_flips = [tuple(map(int, p[1:-1].split(","))) for p in parts[1:-1]]

    return (final_state, switch_flips)


def next_state(switches: int, flip: tuple[int, ...]) -> int:
    for idx in flip:
        switches ^= 1 << idx
    return switches


def num_flips(final_state: int, switch_flips: list[tuple[int, ...]]) -> int:
    visited = {0}
    q = deque([(0, 0)])

    while q:
        cur, steps = q.popleft()

        for flip in switch_flips:
            nx = next_state(cur, flip)
            if nx == final_state:
                return steps + 1

            if nx not in visited:
                visited.add(nx)
                q.append((nx, steps + 1))

    return -1


def main(data: str) -> None:
    rows = data.strip().split("\n")
    ans = 0
    for row in rows:
        fs, sf = parse_row(row)
        res = num_flips(fs, sf)
        ans += res
    print(f"Answer : {ans}")
