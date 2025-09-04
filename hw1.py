from pathlib import Path

import os, shutil, sys

def ensure_dir(directory):
    os.makedirs(directory, exist_ok=True)
    return True

def copy_file(file, dist):
    file = Path(file)
    dist = Path(dist)

    ensure_dir(dist)
    subdir = file.suffix.lstrip(".")
    sub_dist = dist / subdir

    ensure_dir(sub_dist)
    target = sub_dist / file.name
    if not target.exists():
        shutil.copy2(file, target)

def read_dir_recursively(directory, dist):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            read_dir_recursively(item_path, dist)
        else:
            copy_file(item_path, dist)

def main():
    try:
        if len(sys.argv) < 2:  
            raise ValueError("Input directory argument is required.")
        else:
            full_path = os.path.abspath(sys.argv[1])
            print(f"Working with directory: {full_path}")
    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        if len(sys.argv) > 3:  
            raise ValueError("Too many arguments. \n" \
            "Usage: python hw1.py <input_dir> or python hw1.py <input_dir> <output_dir>")
    except ValueError as e:
        print(f"Error: {e}")
        return

    if len(sys.argv) == 2:
        inp_dir = sys.argv[1]
        out_dir = 'dist'
    else:
        inp_dir = sys.argv[1]
        out_dir = sys.argv[2]

    read_dir_recursively(inp_dir, out_dir)

    print("Files copied successfully.")

if __name__ == "__main__":
    main()