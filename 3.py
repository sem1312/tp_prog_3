lista = [1,1,1,1,1]
i=0
try:
  i = int(input("que indice quiere acceder "))
except IndexError:
  print("indice no valido")
finally:
  print(lista[i])
