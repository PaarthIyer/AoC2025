import numpy as np
from scipy.signal import convolve2d


def main(data: str) -> None:
    grid = np.array(
        [[0 if ch == "." else 1 for ch in row] for row in data.split()], dtype=np.int8
    )

    kernel = np.ones((3, 3), dtype=np.int8)
    kernel[1, 1] = 0
    ngh = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)

    ans = np.sum((grid == 1) & (ngh < 4))
    print("Answer:", ans)
