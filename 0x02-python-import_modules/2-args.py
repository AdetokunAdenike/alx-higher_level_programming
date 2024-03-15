#!/usr/bin/python3

#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
