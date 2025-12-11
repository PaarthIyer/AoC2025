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


def find_dependency(graph, node1, node2) -> tuple[str, str] | tuple[None, None]:
    if count_paths(graph, node1, node2) > 0:
        return (node1, node2)

    if count_paths(graph, node2, node1) > 0:
        return (node2, node1)

    # ideally shouldn't reach here
    return (None, None)


def main(data: str) -> None:
    graph = {"out": []}
    rows = data.splitlines()
    for row in rows:
        node, children = row.split(":")
        graph[node] = children.split()

    fft_dac_order = find_dependency(graph, "fft", "dac")

    ans = 1

    ans *= count_paths(graph, "svr", fft_dac_order[0])
    ans *= count_paths(graph, fft_dac_order[0], fft_dac_order[1])
    ans *= count_paths(graph, fft_dac_order[1], "out")
    print(f"Answer : {ans}")
