'''
Biblioteca de funções nativas do Python
> os
> sys
> math
> random
> datetime
> collections
> json
'''
import os
import math

x = 16
raiz_quad = math.sqrt(x)
print("Raiz quadrada de ", x, " é igual a ", raiz_quad)

angulo = 45
seno = math.sin(angulo)
print("Seno de ", angulo, " é igual a ", seno)

diretorio = os.getcwd()
print("Diretório atual: ", diretorio)

# os.system("cls")  # Use "dir" no Windows

lista = [10, 20, 30]
tam = len(lista)
print("A lista ", lista, "tem tamanho: ", tam)

soma = sum(lista)
print("A lista ", lista, " tem a somatória igual a ", soma)

os.system("cls")