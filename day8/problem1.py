from collections import defaultdict, deque
import heapq
from math import prod

K = 1000


def coord_dist(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> int:
    return sum((c1[i] - c2[i]) ** 2 for i in (0, 1, 2))


def get_top_k_pairs(coords: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    top_k = []
    num_pts = len(coords)
    for i in range(num_pts - 1):
        for j in range(i + 1, num_pts):
            dist = -coord_dist(coords[i], coords[j])
            if len(top_k) < K:
                heapq.heappush(top_k, (dist, i, j))
            else:
                heapq.heappushpop(top_k, (dist, i, j))
    return [(i, j) for _, i, j in sorted(top_k, key=lambda x: -x[0])]


def connected_components(
    edges: list[tuple[int, int]], num_nodes: int
) -> list[set[int]]:
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    vis = set()
    comps = []

    for n in range(num_nodes):
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

    return comps


def main(data: str) -> None:
    coords = [tuple(int(c) for c in row.split(",")) for row in data.split()]
    num_nodes = len(coords)
    edges = get_top_k_pairs(coords)
    comps = connected_components(edges, num_nodes)
    comp_sizes = sorted([len(comp) for comp in comps], reverse=True)
    if len(comp_sizes) >= 3:
        ans = comp_sizes[0] * comp_sizes[1] * comp_sizes[2]
    else:
        ans = prod(comp_sizes)

    print(f"Answer : {ans}")
