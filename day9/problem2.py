def min_max(pt1: tuple[int, int], pt2: tuple[int, int]) -> tuple[int, int, int, int]:
    x1, y1 = pt1
    x2, y2 = pt2
    return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))


def largest_rect(pts: list[tuple[int, int]]) -> int:
    n = len(pts)
    largest_area = 0
    segments = []
    for i in range(n):
        segments.append(min_max(pts[i], pts[((i + 1) % n)]))

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = min_max(pts[i], pts[j])
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            if area <= largest_area:
                continue

            valid = True
            for xx1, yy1, xx2, yy2 in segments:
                if xx1 < x2 and yy1 < y2 and xx2 > x1 and yy2 > y1:
                    valid = False
                    break
            if valid:
                largest_area = area

    return largest_area


def main(data: str) -> None:
    pts = [tuple(int(x) for x in pt_str.split(",")) for pt_str in data.split()]
    ans = largest_rect(pts)
    print(f"Answer : {ans}")
