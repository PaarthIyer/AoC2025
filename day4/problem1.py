def main(data: str) -> None:
    grid = [[0 if ch == "." else 1 for ch in row] for row in data.split()]
    gl, gh = len(grid[0]), len(grid)

    # pad top and bottom of the grod
    pd = [[0] * gl]
    grid = pd + grid + pd

    # pad sides of the grod
    for i, row in enumerate(grid):
        grid[i] = [0] + row + [0]

    ans = 0

    # iterate through the grid
    for i in range(1, gh + 1):
        for j in range(1, gl + 1):
            if grid[i][j] == 0:
                continue
            ngh = (
                grid[i - 1][j - 1]
                + grid[i - 1][j]
                + grid[i - 1][j + 1]
                + grid[i][j - 1]
                + grid[i][j + 1]
                + grid[i + 1][j - 1]
                + grid[i + 1][j]
                + grid[i + 1][j + 1]
            )
            ans += ngh < 4

    print("\nAnswer : ", ans)
