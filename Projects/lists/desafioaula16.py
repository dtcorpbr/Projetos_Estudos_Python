'''
Crie um programa que peça para que o usuário continue informando números inteiros. O programa deve armazenar tais números em uma lista. O programa deve parar de capturar novos números caso o usuário insira 0 (zero). Ao final, o programa deve informar a quantidade de elementos adicionados na lista, bem como o menor e o maior elementos digitados (desconsiderando o zero).
'''
numeros = []
while True:
    n = int(input("Informe um número inteiro (0 para parar): "))
    if n == 0:
        break
    numeros.append(n)
if numeros:
    print(f"Quantidade de elementos: {len(numeros)}")
    print(f"Menor elemento: {min(numeros)}")
    print(f"Maior elemento: {max(numeros)}")
else:
    print("Nenhum número foi adicionado à lista.")
