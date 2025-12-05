def calc_ans(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort()
    ans = 0
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            ans += cur_end - cur_start + 1
            cur_start, cur_end = start, end

    ans += cur_end - cur_start + 1

    return ans


def main(data: str) -> None:
    fresh, _ = (d.split() for d in data.split("\n\n"))
    fresh_list = [tuple(map(int, f.split("-"))) for f in fresh]

    ans = calc_ans(fresh_list)

    print(f"\nAnswer : {ans}\n")
