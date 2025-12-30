# Maze Solver: BFS Iterative vs. DFS Recursive  

**Course:** Analisis Kompleksitas Algoritma (Complexity Analysis of Algorithms)  
**Semester:** Odd Semester 2025/2026 – Telkom University  

---

## Project Overview

This project is a **desktop-based application** developed to fulfill the requirements of the **Complexity Analysis of Algorithms** course.  
The primary objective is to provide a **practical observation** and a **comparative efficiency study** between **iterative** and **recursive** algorithm implementations.

The project focuses on solving **pathfinding problems in a 2D grid maze** using two distinct approaches:

- **Iterative BFS (Breadth-First Search)**  
  Demonstrates the implementation and analysis of **iterative algorithms**.

- **Recursive DFS (Depth-First Search)**  
  Demonstrates the implementation and analysis of **recursive algorithms**.

---

## Prerequisites & Requirements

To ensure the application runs correctly—especially the **performance analysis module**—the following environment is required:

### System Requirements
- **Python:** 3.10 or higher  
- **Operating System:** Windows, macOS, or Linux (Ubuntu recommended)

### Required Libraries
Install the following libraries to support the GUI, animations, and data visualization:

- **Pygame** – Interactive desktop interface and real-time maze animations  
- **Matplotlib** – Asymptotic complexity graphs based on execution time  
- **NumPy (< 2.0)** – Numerical data handling  

> **Note:**  
> Using **NumPy 1.26.x** is recommended to avoid compatibility issues with Matplotlib on certain systems.

---

## Installation & Setup

Follow these steps to set up the project on your local machine:

### 1️. Clone the Repository
```bash
git clone https://github.com/username/project_AKA.git
cd project_AKA
```

### 2️. Install Dependencies
It is recommended to use `pip`:
```bash
pip install pygame matplotlib "numpy<2"
```

---

## How to Use

Run the main application entry point to access the **Interactive Control Panel**:

```bash
python3 main.py
```

### Interactive Controls

- **Grid Size**
  - Small (11×11)
  - Medium (25×25)
  - Large (51×51)

- **Maze Type**
  - **Generate Random**  
    Creates a random maze using *Recursive Backtracking*
  - **Populate Grid**  
    Creates an empty maze (ideal for **BFS worst-case testing**)

- **Algorithm Selection**
  - BFS (Iterative)
  - DFS (Recursive)

- **Run Full Analysis**
  - Automatically benchmarks both algorithms for input sizes up to **10,000 cells**  
    (up to a **100 × 100** grid)
  - Generates a **comparison graph**

---

## Complexity Analysis

This project implements theoretical concepts from the course:

- **BFS (Iterative)**  
  Analyzed using the **summation method** for iterative loops.  
  Typically shows **O(n)** complexity, where *n* is the number of cells.

- **DFS (Recursive)**  
  Analyzed using **recurrence relations**.  
  While theoretically **O(n)**, the recursive depth is limited by the system stack size.

### Results
The application generates:
- A **performance comparison graph**
- A **summary `.txt` file**

All outputs are stored in the `hasil_analisis/` folder and labeled with a **timestamp** for unique identification.

---

## Project Structure

```text
project_AKA/
│
├── main.py              # Application entry point
├── maze_logic.py        # BFS/DFS algorithms and maze generation
├── visualizer.py        # Pygame-based GUI and animation manager
├── analysis.py          # Automated benchmarking & Matplotlib plotting
├── hasil_analisis/      # Auto-generated graphs and execution logs
```

---

## Authors

- **Wawan Saputra**
- **Moh. Dzaki Ayatillah**
- **M. Rayhan Ramadhan Afdhani**

This project is submitted as a **major assignment** for the  
**Analisis Kompleksitas Algoritma** course at **Telkom University**.
