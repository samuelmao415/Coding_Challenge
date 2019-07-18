#better solution
class Solution(object):
    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def numIslandsDFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc)


##other solution





class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # idea is to make connected components count 1 only by making them 0 once visited
        self.sum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print('looping at column: ', col)
                print('looping at row: ', row)
                self.sum += self.find_islands(grid, row, col)
                print('sum',self.sum)
        return self.sum

    def find_islands(self, grid,i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            print('found land at row and column: ', i, j)
            print('grid: ',grid[i][j])
            grid[i][j] = "0"
            # go top left right bottom
            # make all 1's 0 till all connected becomes zero
            # then return 1 as all connected componets forms one island
            # done
            self.find_islands(grid, i + 1, j)
            self.find_islands(grid, i, j-1)
            self.find_islands(grid, i-1, j)
            self.find_islands(grid, i, j + 1)
            print('return 1','i & j: ', i,j)
            return 1
        print('return 0 ')
        return 0

example = Solution()
# 11110
# 11010
# 11000
# 00000
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
example.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
