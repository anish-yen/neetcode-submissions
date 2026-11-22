from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # used in your bounds check
        minutes = 0                         # incremented after each BFS level
        q= deque()
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counter+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and counter > 0: #stop when rotten all origins 
            level_size = len(q) #every minute tracking

        # Process one minute at a time


            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        counter -= 1
                        q.append((nr, nc))

            minutes += 1

        return minutes if counter == 0 else -1



        #at each minute the queue holds oranges just became rotten