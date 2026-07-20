class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r, c = q.popleft()
            val = grid[r][c] + 1
            for d1, d2 in dir:
                x, y = r + d1, c + d2
                if x >=0 and y >=0 and x < rows and y < cols and grid[x][y] == INF:
                    grid[x][y] = val
                    q.append((x, y))
        
