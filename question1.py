import sys
try:
    if len(sys.argv) != 3:
        raise ValueError
    Argumento_uno = sys.argv[1]
    Argumento_dos = sys.argv[2]
    load_per_support = float(Argumento_uno) / float(Argumento_dos)
    if Argumento_dos == "0":
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        print(f"Load per support: {load_per_support:.2f}N")
except ValueError:
    print("Error: Invalid input! Enter numeric values only.")

