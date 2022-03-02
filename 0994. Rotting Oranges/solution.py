from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [0, 1, 0, -1, 0]
        oranges = 0
        
        q1 = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q1.append((i,j))
                elif grid[i][j] == 1:
                    oranges += 1
        
        if oranges == 0:
            return 0
        
        minutes = 0
        q2 = deque()
        while q1:
            r, c = q1.pop()
            for i in range(4):
                nr, nc = r+dirs[i], c+dirs[i+1]
                if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != 1: continue
                grid[nr][nc] = 2
                oranges -=1
                q2.append((nr,nc))
            if not q1:
                minutes += 1
                q1 = q2.copy()
                q2.clear()
                #print(minutes)
                #print(oranges)
                #print(q1)
                #print(q2)
        
        if oranges > 0:
            return -1
        else:
            return minutes-1