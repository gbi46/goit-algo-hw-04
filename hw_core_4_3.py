import os, pathlib, sys
from colorama import Fore

def show_dir_structure(dir, indent=0):

    structure = ""

    if not os.path.exists(dir):
        return f"{Fore.RED}Error: path {dir} nicht exists"
    
    if not os.path.isdir(dir):
        return f"{Fore.RED}Error: {dir} is not a directory"
    
    dir = pathlib.Path(dir)

    try:
        with os.scandir(dir) as entries:
            for entry in entries:
                if entry.is_dir():
                    color = Fore.BLUE
                else:
                    color = Fore.LIGHTYELLOW_EX

                structure += ' ' * indent + color + "|--" + entry.name + "\n"

                if entry.is_dir():
                    structure += show_dir_structure(entry.path, indent + 4)
    except PermissionError as e:
        structure += f"No permission to {dir}: {e}"

    return structure + Fore.RESET

def main():
    dir = sys.argv[1]
    print(show_dir_structure(dir))

if __name__ == "__main__":
    main()