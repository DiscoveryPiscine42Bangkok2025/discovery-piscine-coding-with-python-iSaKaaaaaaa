import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, "r") as f:
                board_str = f.read()
            checkmate(board_str)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
