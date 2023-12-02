#!/usr/bin/python3
"""Perimeter of an island"""


def findsingleperimeter(grid, pos):
    """Get the relative perimeter of one square"""
    per = 0
    if pos[0] == 0 or pos[0] == len(grid) - 1:
        return 0
    if pos[1] == 0 or pos[1] == len(grid[0]) - 1:
        return 0
    if grid[pos[0]-1][pos[1]] == 0:
        per += 1
    if grid[pos[0]+1][pos[1]] == 0:
        per += 1
    if grid[pos[0]][pos[1]+1] == 0:
        per += 1
    if grid[pos[0]][pos[1]-1] == 0:
        per += 1

    return per


def island_perimeter(grid):
    """inds the perimeter of the island in the grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += findsingleperimeter(grid, (i, j))
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
