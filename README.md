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
