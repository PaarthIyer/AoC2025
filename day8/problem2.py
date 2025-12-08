K = 1000


def get_edges(coords: list[tuple[int, int, int]]) -> int:
    distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1, z1 = coords[i]
            x2, y2, z2 = coords[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((dist, i, j))
    distances.sort()
    edges = [(a, b) for _, a, b in distances]
    return edges


def spanning_tree_last_edge(edges: list[tuple[int, int]]) -> tuple[int, int]:
    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    last_edge = None
    for edge in edges:
        a, b = edge
        if union(a, b):
            last_edge = edge

    return last_edge


def main(data: str) -> None:
    coords = [tuple(int(c) for c in row.split(",")) for row in data.split()]
    edges = get_edges(coords)
    last_edge = spanning_tree_last_edge(edges)
    ans = coords[last_edge[0]][0] * coords[last_edge[1]][0]
    print(f"Answer : {ans}")
