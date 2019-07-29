#better solution

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]




def find_island(grid,i,j):
    if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1':
        grid[i][j] = '0'
        find_island(grid, i+1,j)
        find_island(grid, i, j-1)
        find_island(grid, i-1, j)
        find_island(grid, i, j+1)
        return 1
    return 0

islands = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
            islands += find_island(grid,row,col)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find_island(grid,i,j):
            if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                find_island(grid, i+1,j)
                find_island(grid, i, j-1)
                find_island(grid, i-1, j)
                find_island(grid, i, j+1)
                return 1
            return 0
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    islands += find_island(grid,row,col)
        return(islands)
     
