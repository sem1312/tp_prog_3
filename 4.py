n1=0
n2=0
try:
  n1 = float(input("ingrese un numero "))
  n2 = float(input("ingrese otro numero "))
except TypeError:
  print("tipo de dato invalido")
finally:
  print("el resultado es: ", n1+n2)
