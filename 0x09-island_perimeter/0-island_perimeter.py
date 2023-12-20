#!/usr/bin/python3
'''module: 5-island_perimeter
'''


def island_perimeter(grid):
    '''
    computes the perimeter of the island described in the grid.
    '''
    perimeter = 0

    # check for cell in grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # check if the cell has water on any of its four sides
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
