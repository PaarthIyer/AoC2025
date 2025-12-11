from collections import deque, defaultdict


def main(data: str) -> None:
    edges = {"out": []}
    rows = data.splitlines()
    for row in rows:
        st, rs = row.split(":")
        edges[st] = rs.split()

    depths = {"you": 0}

    q = deque()
    q.append("you")

    while len(q) > 0:
        cur = q.popleft()
        for child in edges[cur]:
            depths[child] = depths[cur] + 1
            q.append(child)

    inv_depths = defaultdict(list)
    for k, v in depths.items():
        inv_depths[v].append(k)

    paths = defaultdict(int)
    paths["you"] = 1
    max_depth = max(inv_depths.keys())

    for i in range(max_depth + 1):
        for node in inv_depths[i]:
            for ch in edges[node]:
                paths[ch] += paths[node]

    ans = paths["out"]
    print(f"Answer : {ans}")
