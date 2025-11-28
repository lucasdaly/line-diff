import os

def normalized(line: str) -> str:
    return line.lstrip()

def preprocess():
    file = input("Enter a file to scan: ").strip()

    new_path = os.path.join("test folder", f"{file} New.java")
    old_path = os.path.join("test folder", f"{file} Old.java")

    new_lines = []
    old_lines = []

    try:
        with open(new_path, "r", encoding="utf-8") as f_new:
            for line in f_new:
                normalize = normalized(line)
                new_lines.append(normalize)
    except FileNotFoundError:
        print(f"An error occured. Could not open: {new_path}")
    
    try:
        with open(old_path, "r", encoding="utf-8") as f_old:
            for line in f_old:
                normalize = normalized(line)
                old_lines.append(normalize)
    except FileNotFoundError:
        print(f"An error occured. Could not open: {old_path}")
    
    print(new_lines)
    print("-")
    print(old_lines)

if __name__ == "__main__":
    preprocess()