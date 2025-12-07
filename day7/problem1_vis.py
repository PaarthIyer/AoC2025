def vis(base, ind) -> str:
    st = list(base)
    for i in ind:
        st[i] = "|"
    return "".join(st)


def main(data: str) -> None:
    rows = data.split()
    beams = [len(rows[0]) // 2]
    splitters = rows[2::2]

    num_splits = 0

    print(vis("." * len(rows[0]), beams))
    for srow in splitters:
        new_beams = []
        for beam in beams:
            if srow[beam] == "^":
                num_splits += 1
                if beam - 1 not in new_beams:
                    new_beams.append(beam - 1)
                if beam + 1 not in new_beams:
                    new_beams.append(beam + 1)
            else:
                if beam not in new_beams:
                    new_beams.append(beam)
        beams = new_beams
        print(vis(srow, beams))
        print(vis("." * len(rows[0]), beams))
    ans = num_splits
    print(f"\nAnswer : {ans}\n")
