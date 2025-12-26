import time
import matplotlib.pyplot as plt
import os
import sys
from datetime import datetime
from maze_logic import MazeLogic

def measure_performance():
    output_folder = "hasil_analisis"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
    bfs_times = []
    dfs_times = []

    print(f"[{timestamp}] Memulai pengambilan data performa...")
    
    for s in sizes:
        n = s * s
        m = MazeLogic(s, s)
        m.generate_random_maze()
        
        # Penanganan khusus Rekursif sesuai materi
        sys.setrecursionlimit(max(20000, n * 2)) 

        # Ukur BFS Iteratif
        start_t = time.perf_counter()
        m.bfs_iterative((0,0), (s-1, s-1))
        bfs_times.append(time.perf_counter() - start_t)

        # Ukur DFS Rekursif
        start_t = time.perf_counter()
        try:
            m.dfs_recursive((0,0), (s-1, s-1))
            dfs_times.append(time.perf_counter() - start_t)
        except RecursionError:
            dfs_times.append(None)

    # 3. Menyimpan Grafik dengan Nama Unik
    plt.figure(figsize=(10, 6))
    plt.plot([s*s for s in sizes], bfs_times, marker='o', label='BFS (Iteratif)')
    plt.plot([s*s for s in sizes], [t for t in dfs_times if t is not None], marker='s', label='DFS (Rekursif)')
    
    plt.xlabel('Ukuran Masukan (Total Sel n)')
    plt.ylabel('Running Time (Detik)')
    plt.title(f'Perbandingan Running Time ({timestamp})')
    plt.grid(True)
    plt.legend()
    
    graph_filename = f"grafik_performa_{timestamp}.png"
    graph_path = os.path.join(output_folder, graph_filename)
    plt.savefig(graph_path)
    plt.close()

    # 4. Menyimpan Data Teks dengan Nama Unik
    text_filename = f"hasil_eksekusi_{timestamp}.txt"
    data_path = os.path.join(output_folder, text_filename)
    with open(data_path, 'w') as f:
        f.write(f"HASIL ANALISIS RUNNING TIME - {timestamp}\n")
        f.write("==========================================\n\n")
        f.write(f"{'n (Total Sel)':<15} | {'BFS (detik)':<15} | {'DFS (detik)':<15}\n")
        f.write("-" * 50 + "\n")
        for i in range(len(sizes)):
            n_val = sizes[i] * sizes[i]
            bfs_val = f"{bfs_times[i]:.6f}"
            dfs_val = f"{dfs_times[i]:.6f}" if dfs_times[i] is not None else "Error/Limit"
            f.write(f"{n_val:<15} | {bfs_val:<15} | {dfs_val:<15}\n")
    
    print(f"Berhasil! File disimpan sebagai:")
    print(f" - {graph_path}")
    print(f" - {data_path}")