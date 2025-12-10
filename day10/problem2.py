from numpy.typing import NDArray
import pulp
import numpy as np


def parse_row(row: str):
    parts = row.split(" ")
    switch_presses = [tuple(map(int, p[1:-1].split(","))) for p in parts[1:-1]]
    joltages = np.array([int(x) for x in parts[-1][1:-1].split(",")])

    swith_matrix = np.zeros((len(joltages), len(switch_presses)), dtype=int)
    for col, press_group in enumerate(switch_presses):
        swith_matrix[press_group, col] = 1

    return (swith_matrix, joltages)


def num_switch_presses(switch_matrix: NDArray, joltage):
    """
    This becomes a LP with constraints.
    All values are non negative integers.
    A -> 0/1 matrix. Denotes the counters increased when the ith switch is pressed.
    B -> The required joltages.
    X -> Number of times to press each switch.

    A X = B

    Need to maximize sum(x_i).
    """
    m, n = switch_matrix.shape

    prob = pulp.LpProblem("MinSumSolution", pulp.LpMinimize)

    # Create integer variables X_i >= 0
    X = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]

    # minimize sum(X)
    prob += pulp.lpSum(X)

    # constraints: A X = B
    for i in range(m):
        prob += pulp.lpSum(switch_matrix[i, j] * X[j] for j in range(n)) == joltage[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    return np.array([var.value() for var in X], dtype=int)


def main(data: str) -> None:
    rows = data.strip().split("\n")
    ans = 0
    for row in rows:
        sp, jl = parse_row(row)
        res = num_switch_presses(sp, jl)
        ans += sum(res)
    print(f"Answer : {ans}")
