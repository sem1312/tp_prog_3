try:
    n1 = float(input("ingrese el numero a dividir "))
    n2 = float(input("por cuanto quiere dividirlo "))
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print(n1/n2)

