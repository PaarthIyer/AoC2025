def largest_joltage(bank: list[int], num_batts=12) -> int:
    joltage = [bank[0]]
    can_reject = len(bank) - num_batts

    for i, bat in enumerate(bank[1:]):
        if joltage[-1] >= bat:
            if len(joltage) < num_batts:
                joltage.append(bat)
            else:
                can_reject -= 1
            continue

        while len(joltage) > 0 and can_reject > 0 and bat > joltage[-1]:
            joltage.pop()
            can_reject -= 1

        if can_reject == 0:
            joltage.extend(bank[i + 1 :])
            break

        joltage.append(bat)

    jlt = 0

    for j in joltage:
        jlt = jlt * 10 + j

    return jlt


def main(data: str) -> None:
    data = data.split()
    banks = [[int(k) for k in d] for d in data]
    joltages = list(map(largest_joltage, banks))
    ans = sum(joltages)

    print(f"\nAnswer : {ans}\n")
