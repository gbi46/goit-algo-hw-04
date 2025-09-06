# File Sorter & Koch Snowflake Drawer

This repository contains **two Python programs**:

1. **File Sorter** – Organizes files from an input directory into a destination directory based on their file extensions.  
2. **Koch Snowflake Drawer** – Generates a Koch snowflake fractal drawing **without Tkinter**.  
Output as an **SVG file** (no dependencies).    

---

## Installation

Both programs require **Python 3.7+**.  
Check your Python version:

```bash
python --version
```

If you have `python3` instead of `python`, use that in all commands below.

### Dependencies

- **File Sorter**: uses only the Python standard library (`os`, `shutil`, `pathlib`, `sys`).  
- **Koch Snowflake Drawer**:  
  - For the **SVG version** → no additional packages required.

---

## 1. File Sorter

### Usage

Run the script with:

```bash
python hw1.py <input_dir> [output_dir]
```

- `<input_dir>`: Path to the folder you want to organize (**required**).  
- `[output_dir]`: Path to the destination folder (**optional**, defaults to `dist`).  

### Example

```bash
python hw1.py ~/Downloads
```

This will:
- Read all files in `~/Downloads` (recursively).  
- Copy them into `./dist/` with subfolders by extension:  
  - `dist/jpg` for `.jpg` files  
  - `dist/txt` for `.txt` files  
  - `dist/no_ext` for files without an extension  

```bash
python hw1.py ~/Downloads ~/OrganizedFiles
```

This saves sorted files into `~/OrganizedFiles`.

---

## 2. Koch Snowflake Drawer

This program generates a **Koch snowflake** and saves it as a file.  
No window is opened.

### Usage

Run:

```bash
python hw2.py
```

The program will ask for recursion depth:

```
Enter recursion depth (e.g. 0-6):
```

- **Depth 0** → simple triangle  
- **Depth 1** → triangle with bumps  
- **Depth 4–6** → detailed fractal (larger file, takes longer to compute)  

### Output

- **SVG version**: produces `koch_snowflake.svg` → open in browser or image viewer.

# Comparison of Sorting Algorithms: Insertion, Merge, and Timsort

This project provides an empirical comparison of three sorting algorithms:

1. **Insertion Sort** – simple quadratic algorithm.  
2. **Merge Sort** – classical divide-and-conquer algorithm with runtime `O(n log n)`.  
3. **Timsort** – hybrid algorithm used in Python (`list.sort()` and `sorted()`), combining ideas of insertion sort and merge sort.  

---

## Installation

Requirements:

- Python 3.7+
- Libraries: `pandas`, `matplotlib` (for saving and visualizing results)

Install dependencies:

```bash
pip install pandas matplotlib
```

---

## Running the Benchmark

Run the script:

```bash
python hw3.py
```

The script performs:

- Generation of arrays of various sizes (1000–12000 elements)  
- Testing algorithms on random, sorted, reversed, and nearly sorted arrays  
- Saving results into `sorting_benchmark_results.csv`  
- Creating a plot `sorting_benchmark_random.png` for the random dataset  

---

## Theoretical Complexity

- **Insertion Sort**:  
  - Best case (nearly sorted data): `O(n)`  
  - Average and worst cases: `O(n²)`  

- **Merge Sort**:  
  - Always: `O(n log n)`  
  - Requires additional memory  

- **Timsort**:  
  - Best case: `O(n)` (already or nearly sorted data)  
  - Worst case: `O(n log n)`  
  - Exploits monotone runs and combines insertion with merging for optimal performance  

---

## Empirical Results

- **Insertion Sort**: very slow on random and reversed arrays; feasible only for small inputs or nearly sorted data.  
- **Merge Sort**: consistent `O(n log n)` behavior, but slower than Timsort due to lack of optimizations.  
- **Timsort**: consistently fastest, especially on sorted and nearly sorted datasets, thanks to its hybrid design.  

Example plot for random data:  

`sorting_benchmark_random.png`

---

## Conclusion

The results confirm theoretical complexity:  
- Insertion Sort quickly loses efficiency on large inputs.  
- Merge Sort is reliable but not the fastest.  
- **Timsort combines the best aspects of both approaches** and is significantly more efficient in practice. This is why Python programmers almost always rely on the built-in `sorted()` or `.sort()` rather than implementing sorting manually.
