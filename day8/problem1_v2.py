from collections import defaultdict, deque


K = 1000


def solve(coords: list[tuple[int, int, int]]) -> int:
    distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1, z1 = coords[i]
            x2, y2, z2 = coords[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((dist, i, j))
    distances.sort()
    edges = [(a, b) for _, a, b in distances[:K]]

    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    vis = set()
    comps = []

    for n in range(len(coords)):
        if n not in vis:
            q = deque([n])
            vis.add(n)
            curr_comp = {n}
            while q:
                curr = q.popleft()
                for nbr in adj[curr]:
                    if nbr not in vis:
                        vis.add(nbr)
                        q.append(nbr)
                        curr_comp.add(nbr)
            comps.append(curr_comp)

    comp_sizes = [len(comp) for comp in comps]
    comp_sizes.sort(reverse=True)

    return comp_sizes[0] * comp_sizes[1] * comp_sizes[2]


def main(data: str) -> None:
    coords = [tuple(int(c) for c in row.split(",")) for row in data.split()]
    ans = solve(coords)
    print(f"Answer : {ans}")
