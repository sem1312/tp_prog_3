n=0
try:
    n = float(input("ingrese el numero que quiere convertir a entero"))
except ValueError:
    print("no se puede")
finally:
    integer = int(n)
