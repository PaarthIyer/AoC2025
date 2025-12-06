def main(data: str) -> None:
    lines = [line.split() for line in data.splitlines()]
    nums, ops = lines[:-1], lines[-1]
    num_operands = len(nums)
    ans = 0
    for i, op in enumerate(ops):
        if op == "*":
            step = 1
            for j in range(num_operands):
                step *= int(nums[j][i])
        else:
            step = 0
            for j in range(num_operands):
                step += int(nums[j][i])

        ans += step

    print(f"\nAnswer : {ans}\n")
