import numpy as np
from scipy.signal import convolve2d


def main(data: str) -> None:
    grid = np.array(
        [[0 if ch == "." else 1 for ch in row] for row in data.split()], dtype=np.uint8
    )

    kernel = np.ones((3, 3), dtype=np.uint8)
    kernel[1, 1] = 0

    ans = 0

    # Loop until no more removals
    while True:
        ngh = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)

        remove_mask = (grid == 1) & (ngh < 4)

        # No removals
        if not np.any(remove_mask):
            break

        ans += np.sum(remove_mask)

        grid[remove_mask] = 0

    print("\nAnswer :", ans)
