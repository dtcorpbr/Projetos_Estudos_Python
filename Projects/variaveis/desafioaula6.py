# Declare quatro variáveis, id, do tipo inteiro, nome, do
# tipo string, salário, do tipo float e a variável brasileiro
# do tipo bool.
# > Peça para que o usuário informe os dados acima.
# > Ao final, imprima tudo na tela utilizando f-strings.

id = 0
nome = ""
salario = 0.00
nacionalidade = ""

id = int(input("Digite seu id: "))
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
nacionalidade = bool(input("É brasileiro? Digite S (sim) ou N (não)"))

print("**************************************")
print("Seu id é: ", id)
print("**************************************")
print("Seu nome é: ", nome)
print("**************************************")
print("Seu salário é: ", salario)
print("**************************************")
print("É brasileiro? ", nacionalidade)
print("**************************************")