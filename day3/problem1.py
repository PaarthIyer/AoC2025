def largest_joltage(bank: list[int]) -> int:
    lb1 = 0
    lb2 = 0
    lb1 = max(bank[:-1])
    lb2 = max(bank[bank[:-1].index(lb1) + 1 :])

    return 10 * lb1 + lb2


def main(data: str) -> None:
    data = data.split()
    banks = [[int(k) for k in d] for d in data]
    joltages = list(map(largest_joltage, banks))
    ans = sum(joltages)

    print(f"\nAnswer : {ans}\n")
