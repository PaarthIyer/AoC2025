def parse_boxes(boxes_: list[str]):
    boxes = {}
    for i, b in enumerate(boxes_):
        bar = 0
        bx = []
        for rw in b.split("\n")[1:]:
            prw = tuple(1 if x == "#" else 0 for x in rw)
            bar += prw[0] + prw[1] + prw[2]
            bx.append(prw)
        bx = tuple(bx)
        boxes[i] = {"box": bx, "area": bar}

    return boxes


def parse_areas(areas_: str):
    areas_ = areas_.strip().split("\n")
    areas = []
    for rw in areas_:
        region, num_bx = rw.split(":")
        region = tuple(map(int, region.split("x")))
        num_bx = tuple(map(int, num_bx.split()))
        areas.append({"region": region, "num_boxes": num_bx})
    return areas


def minimum_area_filter(boxes, areas):
    diff = []
    for ar in areas:
        region_area = ar["region"][0] * ar["region"][1]
        min_box_area = 0
        for box_id, num_boxes in enumerate(ar["num_boxes"]):
            min_box_area += num_boxes * boxes[box_id]["area"]

        if region_area - min_box_area > 0:
            diff.append(ar)
    return diff


def naive_placements(boxes, areas):
    total = 0
    retry = []
    for ar in areas:
        total_boxes = sum(ar["num_boxes"])
        naive = (ar["region"][0] // 3) * (ar["region"][1] // 3)
        if naive >= total_boxes:
            total += 1
        else:
            retry.append(ar)
    return retry, total


def main(data: str) -> None:
    *boxes_, areas_ = data.split("\n\n")
    boxes = parse_boxes(boxes_)
    areas = parse_areas(areas_)
    areas = minimum_area_filter(boxes, areas)
    areas, first_pass = naive_placements(boxes, areas)
    # Turns out this much is actually enough

    assert areas == []
    ans = first_pass
    print(f"Answer : {ans}")
