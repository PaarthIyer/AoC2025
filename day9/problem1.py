def largest_rect(pts: list[tuple[int, int]]) -> int:
    largest_area = 0
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            area = (abs((x1 - x2)) + 1) * (abs((y1 - y2)) + 1)
            if area > largest_area:
                largest_area = area
    return largest_area


def main(data: str) -> None:
    pts = [tuple(int(x) for x in pt_str.split(",")) for pt_str in data.split()]
    ans = largest_rect(pts)
    print(f"Answer : {ans}")
