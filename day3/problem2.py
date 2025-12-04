def largest_joltage(bank: list[int], num_batts: int = 12) -> int:
    joltage = 0
    prev_idx = -1

    for bat in range(num_batts):
        start = prev_idx + 1
        end = -(num_batts - 1 - bat)
        end = end if end != 0 else len(bank)
        next_digit = max(bank[start:end])
        joltage = joltage * 10 + next_digit
        prev_idx = (bank[start:end]).index(next_digit) + start

    return joltage


def main(data: str) -> None:
    data = data.split()
    banks = [[int(k) for k in d] for d in data]
    joltages = list(map(largest_joltage, banks))
    ans = sum(joltages)

    print(f"\nAnswer : {ans}\n")
