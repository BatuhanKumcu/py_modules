
def secure_archive(filename: str, action: str = "read", content: str = "")\
        -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return True, file.read()
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        return False, f"Invalid action: {action}"
    except (FileNotFoundError, PermissionError, OSError) as e:
        return False, f"{e}"


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("selamlar.txt", "write", "selamlar"))
