from math import prod


def ceph_nums(nums: str) -> list[list[int]]:
    ceph = []
    run = []

    for i in range(len(nums[0])):
        str_num = "".join([line[i] for line in nums]).strip()
        if str_num == "":
            ceph.append(run)
            run = []
        else:
            run.append(int(str_num))
    ceph.append(run)
    return ceph


def main(data: str) -> None:
    lines = data.splitlines()
    nums, ops = lines[:-1], lines[-1].split()
    nums = ceph_nums(nums)
    ans = 0
    for i, op in enumerate(ops):
        if op == "*":
            ans += prod(nums[i])
        else:
            ans += sum(nums[i])

    print(f"\nAnswer : {ans}")
