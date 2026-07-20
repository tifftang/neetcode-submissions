class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        mins = 0
        seen = set()
        dir = [(0, 1), (0, -1), (1,0), (-1, 0)]
        while q and fresh:

            for i in range(len(q)):
                x, y = q.popleft()
                for d1, d2 in dir:
                    r, c = x + d1, y + d2
                    if r >= 0 and c >= 0 and r < rows and c < cols and (r, c) not in seen and grid[r][c] == 1:
                        fresh -= 1
                        seen.add((r, c))
                        q.append((r, c))
            mins += 1
        return mins if not fresh else -1