'''
Crie um programa que receba o nome de uma pessoa e sua idade. Caso a idade seja maior ou igual a 18, imprimir nome da pessoa e informar , na tela, que ela é maior de idade. Caso contrário, imprimir o nome da pessoa e informar que ela é menor de idade.
'''
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")