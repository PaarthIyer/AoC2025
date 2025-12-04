def main(data: str) -> None:
    rotations = data.split()

    ptr = 50
    password = 0

    for rt in rotations:
        i = int(rt[1:])
        if rt[0] == "L":
            i *= -1
        ptr = (ptr + i) % 100
        password += ptr == 0

    print(f"\nAnswer : {password}\n")
