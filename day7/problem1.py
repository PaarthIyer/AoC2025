def main(data: str) -> None:
    rows = data.split()
    beams = set()
    beams.add(len(rows[0]) // 2)
    splitters = rows[2::2]

    num_splits = 0

    for srow in splitters:
        new_beams = set()
        for beam in beams:
            if srow[beam] == "^":
                num_splits += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    ans = num_splits
    print(f"\nAnswer : {ans}\n")
