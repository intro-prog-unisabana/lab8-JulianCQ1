import sys
try:
    if len(sys.argv) != 3:
        raise ValueError
    Argumento_uno = sys.argv[1]
    Argumento_dos = sys.argv[2]
   
    if Argumento_dos == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        load_per_support = float(Argumento_uno) / float(Argumento_dos)
        print(f"Load per support point: {load_per_support:.2f}N")
except ValueError:
    print("Error: Invalid input! Enter numeric values only.")

