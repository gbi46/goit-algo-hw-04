import sys

def load_data(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
        sys.exit(1)
    except IOError as e:
        print(f"Error: error while try to read file '{path}' : {e}")
        sys.exit(1)
        
    
def clean_data(file_data: list[str])-> list[str]:
    return [temp.strip() for temp in file_data if temp.strip()]