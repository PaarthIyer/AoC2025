from functools import cache


def count_paths(graph: dict[str, list[str]], start, end) -> int:
    @cache
    def dfs(node: str) -> int:
        if node == end:
            return 1
        if node not in graph:
            return 0

        total = 0
        for child in graph[node]:
            total += dfs(child)

        return total

    return dfs(start)


def main(data: str) -> None:
    graph = {"out": []}
    rows = data.splitlines()
    for row in rows:
        node, children = row.split(":")
        graph[node] = children.split()

    ans = count_paths(graph, "you", "out")
    print(f"Answer : {ans}")
