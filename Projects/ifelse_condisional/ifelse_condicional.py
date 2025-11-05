'''
Crie um progama que receba a nota de uma pessoa. 
Imprima "Aprovado(a)" se a nota for maior ou igual a 7.
Caso contrário, imprima "Reprovado(a)", na tela.'''

nota = float(input("Digite a sua nota: "))

if nota >= 7:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")