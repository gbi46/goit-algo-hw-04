# File Sorter & Koch Snowflake Drawer

This repository contains **two Python programs**:

1. **File Sorter** – Organizes files from an input directory into a destination directory based on their file extensions.  
2. **Koch Snowflake Drawer** – Uses Python's `turtle` graphics (Tkinter) to draw a Koch snowflake fractal.  

---

## Installation

Both programs require **Python 3.7+**.  
Check your Python version:

```bash
python --version
```

If you have `python3` instead of `python`, use that in all commands below.

### Install Tkinter

Both programs use only Python’s **standard library** (`os`, `shutil`, `pathlib`, `sys`, `turtle`).  
The only external dependency is **Tkinter**, which may need installation depending on your OS.

#### Windows
Tkinter is included with the standard Python installer from [python.org](https://www.python.org/downloads/).  
If you see an error like `ModuleNotFoundError: No module named 'tkinter'`, reinstall Python using the **Windows installer** and ensure you check **"tcl/tk and IDLE"** during installation.

#### Ubuntu / Debian
Run:
```bash
sudo apt update
sudo apt install python3-tk
```

#### macOS
Tkinter is included with the official Python installer from [python.org](https://www.python.org/downloads/).  
If you installed Python via Homebrew and Tkinter is missing:
```bash
brew install python-tk
```

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

This program draws a **Koch snowflake fractal** using `turtle` graphics.

### Usage

Run:
```bash
python hw2.py
```

The program will ask for recursion depth:
```
Enter recursion depth (e.g. 0-6):
```

- **Depth 0** → just a triangle  
- **Depth 1** → triangle with bumps  
- **Depth 4–6** → detailed fractal (drawing will take longer)  

### Example

At **depth 3**, the snowflake looks like a symmetric fractal ❄️.

---

## Notes

- The two programs are currently in the **same file (`hw1.py`)**, and both define a `main()` function.  
  - To run the **file sorter**, pass arguments → `python hw1.py <input_dir>`.  
  - To run the **snowflake**, just run `python hw1.py` without arguments.  
- If you prefer them separate, split the code into:  
  - `file_sorter.py`  
  - `koch_snowflake.py`  

---

Now you can organize your files **and** draw fractals with one script!
