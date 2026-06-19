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
        content: str = file.read()
        print(content, end="")
        print("\n---")
        print(f"File '{sys.argv[1]}' closed\n")
        transform: str = content.replace("\n", "#\n")
        if content and not content.endswith("\n"):
            transform += "#"
        file.close()
        print("Transform data:")
        print("---\n")
        print(transform, end="")
        print("\n---")
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_name: str = sys.stdin.readline().strip()
        if new_name:
            new_file: typing.IO[str] = open(new_name, "w")
            new_file.write(transform)
            new_file.close()
            print(f"Saving data to '{new_name}'")
            print(f"data saved in file '{new_name}'")
        else:
            print("No file created. Original file was not changed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}"
              , file=sys.stderr)
