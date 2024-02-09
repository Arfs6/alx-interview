#!/usr/bin/python3
"""Finding the perimeter of an island in a grid.
"""


def _getPartialPerimeter(grid, tileIdx, rowIdx):
    """Gets the perimeter nearby
    Parameters:
    - grid: A list of lists representing the map.
    - tileIdx: Index of the current tile, the tile should represent an ocean.
    rowIdx: Index of the current row.
    Returns:
    - int: An integer representing the island perimeter nearby.
    """
    partialPerimeter = 0
    if tileIdx != 0 and grid[rowIdx][tileIdx - 1] == 1:
        # left tile
        partialPerimeter += 1
    if tileIdx + 1 < len(grid[rowIdx]) and grid[rowIdx][tileIdx + 1] == 1:
        # right tile
        partialPerimeter += 1
    if rowIdx != 0 and grid[rowIdx - 1][tileIdx] == 1:
        # top tile
        partialPerimeter += 1
    if rowIdx + 1 < len(grid) and grid[rowIdx + 1][tileIdx] == 1:
        # bottom tile
        partialPerimeter += 1
    return partialPerimeter


def island_perimeter(grid):
    """Calculates the perimeter of an island.
    Parameters:
    - grid: A grid representing the map containing the island.
    Returns: The perimeter of the island.
    """
    perimeter = 0
    for rowIdx, row in enumerate(grid):
        for tileIdx, tile in enumerate(row):
            if tile == 0:  # If this tile represent an ocean.
                perimeter += _getPartialPerimeter(grid, tileIdx, rowIdx)
    return perimeter
