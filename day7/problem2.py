from collections import Counter


def main(data: str) -> None:
    rows = data.split()
    beams = Counter()
    beams[len(rows[0]) // 2] = 1
    splitters = rows[2::2]

    for srow in splitters:
        new_beams = Counter()
        for beam in beams:
            if srow[beam] == "^":
                new_beams[beam - 1] += beams[beam]
                new_beams[beam + 1] += beams[beam]
            else:
                new_beams[beam] += beams[beam]

        beams = new_beams
    ans = beams.total()
    print(f"\nAnswer : {ans}\n")
