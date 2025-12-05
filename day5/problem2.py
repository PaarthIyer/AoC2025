def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def main(data: str) -> None:
    fresh, _ = (d.split() for d in data.split("\n\n"))
    fresh_list = [tuple(map(int, f.split("-"))) for f in fresh]

    merged_fresh = merge_intervals(fresh_list)
    ans = sum(b - a + 1 for (a, b) in merged_fresh)

    print(f"\nAnswer : {ans}\n")
