class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        
        def area(grid,i,j):
            nonlocal cols, rows
            res = 0
            if 0 <= i <= rows-1 and 0 <= j <= cols-1:
                if grid[i][j] == 1:
                    grid[i][j] = '2'
                    res += area(grid,i-1,j)
                    res += area(grid,i+1,j)
                    res += area(grid,i,j-1)
                    res += area(grid,i,j+1)
                    res += 1
            return res
            
            
        cols = len(grid[0])
        rows = len(grid)
        maxi = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxi = max(maxi, area(grid,i,j))
        return maxi