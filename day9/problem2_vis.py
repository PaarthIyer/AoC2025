import matplotlib.pyplot as plt


def compress(pts):
    x_pts = sorted([p[0] for p in pts])
    y_pts = sorted([p[1] for p in pts])
    x_map = {i: x_pts[i] for i in range(len(x_pts))}
    x_map.update({x_pts[i]: i for i in range(len(x_pts))})
    y_map = {i: y_pts[i] for i in range(len(y_pts))}
    y_map.update({y_pts[i]: i for i in range(len(y_pts))})

    return [(x_map[x], y_map[y]) for x, y in pts]


def main(data: str) -> None:
    pts = [tuple(int(x) for x in pt_str.split(",")) for pt_str in data.split()]
    new_pts = compress(pts)

    plt.plot([p[0] for p in new_pts], [p[1] for p in new_pts])
    plt.savefig("/home/paart/pythoncodes/AoC2025/day9/plot.png")
