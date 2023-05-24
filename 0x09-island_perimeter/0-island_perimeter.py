#!/usr/bin/python3
"""Island Perimeter
"""



def island_perimeter(grid):
    ''' 
    Calculates the perimeter of the island 
    Args:
        grid: 2d containing 0(water) or 1(land)
    Return:
        perimeter
    '''

    perimeter = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] == 1):
                if (row <= 0 or grid[row - 1][col] == 0):
                    perimeter += 1
                    
                if (row >= len(grid) - 1 or grid[row + 1][col] == 0):
                    perimeter += 1
                    
                if (col <= 0 or grid[row][col - 1] == 0):
                    perimeter += 1
                    
                if (col >= len(grid[row]) - 1 or grid[row][col + 1] == 0):
                    perimeter += 1
                    
    return perimeter