import sys
import typing


print("=== Cyber Archives Recovery ===")

if len(sys.argv) < 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1])

        print("---\n")
        print(file.read(), end="")
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
