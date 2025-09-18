import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    zs = "".join([c for c in text if c == "z"])
    if zs:
        print(zs)
    else:
        print("none")