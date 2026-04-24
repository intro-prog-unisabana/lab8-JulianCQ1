import sys
try:
    if len(sys.argv) != 3:
        raise IndexError("Error: Two numeric arguments are required.")
    Argumento_uno = float(sys.argv[1])
    Argumento_dos = float(sys.argv[2])

    if Argumento_dos == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        load_per_support = (Argumento_uno) / (Argumento_dos)
        print(f"Load per support point: {load_per_support:.2f} N")
except ValueError:
        print("Error: Invalid input! Enter numeric values only.")

except Exception as e:
        print(e)