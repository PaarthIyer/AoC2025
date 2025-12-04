def main(data: str) -> None:
    rotations = data.split()

    ptr = 50
    password = 0

    for rt in rotations:
        i = int(rt[1:])
        d = rt[0]
        full_rots = 0

        if i > 100:
            full_rots = i // 100
            i = i % 100

        if d == "L":
            i = -i
            if ptr == 0:
                ptr = 100

        sm = ptr + i
        password += full_rots + (sm >= 100) + (sm <= 0)
        ptr = sm % 100

    print(f"\nAnswer : {password}\n")
