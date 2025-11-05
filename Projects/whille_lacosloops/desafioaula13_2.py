'''
Crie um programa que peça ao usuário para digitar um número positivo e imprima todos os números pares de 0 até esse número.
'''
numero = int(input("Digite um número positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, digite um número positivo!")
else:
    print(f"Números pares de 0 até {numero}:")

    i = 0  # contador inicial
    while i <= numero:
        if i % 2 == 0:
            print(i)
        i += 1  # incrementa o contador
