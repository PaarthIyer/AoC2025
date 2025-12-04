def geq_valid(s: str) -> int:
    # Keep track of number
    found = None
    md = len(s) // 2

    for i in range(1, md + 1):
        # skip i if coprime
        if len(s) % i != 0:
            continue
        # check high againt the rest of the chunks
        high = int(s[:i])
        for j in range(1, len(s) // i):
            chk = int(s[j * i : (j + 1) * i])
            if high > chk:
                break
            if high < chk:
                high += 1
                break
        # get the next number with the repetition made with this chunk size
        num = int(str(high) * (len(s) // i))
        if found is None or num < found:
            found = num
    if found is None:
        found = int("1" + "0" * md)
    return found if found >= 11 else 11


def next_valid(n: int) -> int:
    return geq_valid(str(n + 1))


def main(data: str) -> None:
    s = data.strip()
    ranges = [tuple(part.split("-")) for part in s.split(",") if part]
    ans = 0
    for r in ranges:
        j = geq_valid(r[0])
        while j <= int(r[1]):
            ans += j
            j = next_valid(j)

    print(f"\nAnswer : {ans}\n")
