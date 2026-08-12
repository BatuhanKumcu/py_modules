import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file: typing.IO[str] = open(sys.argv[1])
            print("---\n")
            content: str = file.read()
            print(content, end="")
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.\n")
            transform: str = content.replace("\n", "#\n")
            if content and not content.endswith("\n"):
                transform += "#"
            file.close()
            print("Transform data:")
            print("---\n")
            print(transform, end="")
            print("\n---")
            new_name: str = input("Enter new file name (or empty): ")
            if new_name:
                print(f"Saving data to '{new_name}'")
                try:
                    new_file: typing.IO[str] = open(new_name, "w")
                    new_file.write(transform)
                    new_file.close()
                    print(f"data saved in file '{new_name}'")
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Error opening file '{sys.argv[1]}': {e}")
                    print("Data not saved.")
            else:
                print("Not saving data.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
