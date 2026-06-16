import sys

print("=== Command Quest ===")
print("Program name:", sys.argv[0])

if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    print("Arguments provided:", len(sys.argv) - 1)

    for i in range(1, len(sys.argv)):
        print("Argument", i, ":", sys.argv[i])

print("Total arguments:", len(sys.argv))
