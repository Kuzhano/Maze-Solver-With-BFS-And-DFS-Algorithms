import pygame
import sys
from maze_logic import MazeLogic
from analysis import measure_performance

# Warna UI
COLOR_PANEL = (45, 52, 54)
COLOR_BTN = (99, 110, 114)
COLOR_BTN_HOVER = (178, 190, 195)
COLOR_BTN_ACTIVE = (0, 184, 148)
COLOR_TEXT = (255, 255, 255)

class Button:
    def __init__(self, x, y, w, h, text, action_val=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action_val = action_val
        self.is_active = False

    def draw(self, screen, font, mouse_pos):
        color = COLOR_BTN_ACTIVE if self.is_active else (COLOR_BTN_HOVER if self.rect.collidepoint(mouse_pos) else COLOR_BTN)
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        txt = font.render(self.text, True, COLOR_TEXT)
        screen.blit(txt, (self.rect.centerx - txt.get_width()//2, self.rect.centery - txt.get_height()//2))

class MazeApp:
    def __init__(self):
        pygame.init()
        self.window_w, self.window_h = 1000, 700
        self.screen = pygame.display.set_mode((self.window_w, self.window_h))
        self.font = pygame.font.SysFont("Arial", 18)
        self.clock = pygame.time.Clock()
        
        # State Aplikasi
        self.rows, self.cols = 21, 21
        self.maze = MazeLogic(self.rows, self.cols)
        self.selected_algo = "BFS"
        self.visited = {}
        self.final_path = []
        
        # Inisialisasi Tombol
        self.buttons = [
            Button(750, 50, 200, 40, "Small (11x11)", (11, 11)),
            Button(750, 100, 200, 40, "Medium (25x25)", (25, 25)),
            Button(750, 150, 200, 40, "Large (51x51)", (51, 51)),
            Button(750, 250, 200, 40, "Generate Random"),
            Button(750, 300, 200, 40, "Populate Empty Grid"),
            Button(750, 400, 90, 40, "BFS", "BFS"),
            Button(860, 400, 90, 40, "DFS", "DFS"),
            Button(750, 500, 200, 60, "START SEARCH"),
            Button(750, 600, 200, 40, "Run Full Analysis")
        ]
        self.buttons[0].is_active = True # Default Small
        self.buttons[5].is_active = True # Default BFS

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(mouse_pos)

            self.draw(mouse_pos)
            self.clock.tick(60)

    def handle_click(self, pos):
        for btn in self.buttons:
            if btn.rect.collidepoint(pos):
                if "Small" in btn.text or "Medium" in btn.text or "Large" in btn.text:
                    self.rows, self.cols = btn.action_val
                    self.maze = MazeLogic(self.rows, self.cols)
                    for b in self.buttons[:3]: b.is_active = False
                    btn.is_active = True
                    
                elif btn.text == "Generate Random":
                    self.maze.generate_random_maze(); self.visited = {}; self.final_path = []
                    
                elif btn.text == "Populate Empty Grid":
                    self.maze.generate_empty_maze(); self.visited = {}; self.final_path = []
                    
                elif btn.text in ["BFS", "DFS"]:
                    self.selected_algo = btn.action_val
                    self.buttons[5].is_active = (btn.text == "BFS")
                    self.buttons[6].is_active = (btn.text == "DFS")
                    
                elif btn.text == "START SEARCH":
                    self.start_algorithm()
                    
                elif btn.text == "Run Full Analysis":
                    measure_performance()

    def start_algorithm(self):
        self.visited = {}
        self.final_path = []
        
        def callback(node, status):
            self.visited[node] = True
            self.draw(pygame.mouse.get_pos())
            pygame.time.delay(5 if self.rows > 25 else 20)
            for event in pygame.event.get(): pass # Keep window responsive

        if self.selected_algo == "BFS":
            self.final_path = self.maze.bfs_iterative((0,0), (self.rows-1, self.cols-1), callback)
            
        else:
            import sys
            sys.setrecursionlimit(5000)
            self.final_path = self.maze.dfs_recursive((0,0), (self.rows-1, self.cols-1), callback=callback)

    def draw(self, mouse_pos):
        self.screen.fill((236, 240, 241))
        
        # Gambar Area Grid
        grid_area_size = 650
        cell_size = grid_area_size // max(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                color = (44, 62, 80) if self.maze.grid[r][c] == 1 else (255, 255, 255)
                if (r, c) in self.visited: color = (52, 152, 219)
                if (r, c) in self.final_path: color = (251, 197, 49)
                if (r, c) == (0,0): color = (76, 209, 55)
                if (r, c) == (self.rows-1, self.cols-1): color = (232, 65, 24)
                
                pygame.draw.rect(self.screen, color, (25 + c*cell_size, 25 + r*cell_size, cell_size-1, cell_size-1))

        # Gambar Panel Kontrol
        pygame.draw.rect(self.screen, COLOR_PANEL, (700, 0, 300, 700))
        title = self.font.render("MAZE CONTROL PANEL", True, COLOR_TEXT)
        self.screen.blit(title, (750, 20))
        
        for btn in self.buttons:
            btn.draw(self.screen, self.font, mouse_pos)

        pygame.display.flip()