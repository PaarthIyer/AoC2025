def geq_valid_part(s: str) -> int:
    md = len(s) // 2
    if len(s) % 2 != 0:
        return int("1" + "0" * md)

    low = int(s[md:])
    high = int(s[:md])

    return high + (high < low)


def leq_valid_part(s: str) -> int:
    md = len(s) // 2
    if len(s) % 2 != 0:
        return int("9" * md)

    low = int(s[md:])
    high = int(s[:md])

    return high - (high > low)


def main(data: str) -> None:
    s = data.strip()
    ranges = [tuple(part.split("-")) for part in s.split(",") if part]
    ans = 0
    for r in ranges:
        for j in range(geq_valid_part(r[0]), leq_valid_part(r[1]) + 1):
            ans += j
            ans += j * 10 ** (len(str(j)))

    print(f"\nAnswer : {ans}\n")
