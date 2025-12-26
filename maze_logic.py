import random
from collections import deque

class MazeLogic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)] # 1 adalah dinding

    def generate_random_maze(self):
        # Menggunakan algoritma DFS untuk generate maze (Recursive Backtracking)
        def walk(r, c):
            self.grid[r][c] = 0
            dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(dirs)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 1:
                    self.grid[r + dr//2][c + dc//2] = 0
                    walk(nr, nc)
        walk(0, 0)
        self.grid[0][0] = 0
        self.grid[self.rows-1][self.cols-1] = 0

    def generate_empty_maze(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    # BFS ITERATIF - Sesuai materi Analisis Iteratif
    def bfs_iterative(self, start, end, callback=None):
        queue = deque([start])
        visited = {start: None}
        while queue:
            curr = queue.popleft()
            if callback: callback(curr, "visiting")
            
            if curr == end:
                return self._reconstruct_path(visited, end)
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                next_node = (curr[0]+dr, curr[1]+dc)
                
                if (0 <= next_node[0] < self.rows and 0 <= next_node[1] < self.cols and 
                    self.grid[next_node[0]][next_node[1]] == 0 and next_node not in visited):
                    visited[next_node] = curr
                    queue.append(next_node)
        return None

    # DFS REKURSIF - Sesuai materi Analisis Rekursif
    def dfs_recursive(self, curr, end, visited=None, callback=None):
        if visited is None: visited = {curr: None}
        
        if callback: callback(curr, "visiting")
        
        if curr == end:
            return self._reconstruct_path(visited, end)
        
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            next_node = (curr[0]+dr, curr[1]+dc)
            if (0 <= next_node[0] < self.rows and 0 <= next_node[1] < self.cols and 
                self.grid[next_node[0]][next_node[1]] == 0 and next_node not in visited):
                visited[next_node] = curr
                
                path = self.dfs_recursive(next_node, end, visited, callback)
                if path: return path
                
        return None

    def _reconstruct_path(self, visited, curr):
        path = []
        
        while curr is not None:
            path.append(curr)
            curr = visited[curr]
            
        return path[::-1]