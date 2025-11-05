'''
Crie um programa que peça ao usuário para digitar um número inteiro compreendido entre 1 e 7.
 * Imprima o dia da semana correspondente ao número digitado (1 para domingo, 2 para segunda-feira, etc.). Se o número digitado não estiver entre 1 e 7, imprima uma mensagem de erro "número inválido".
'''
dia = int(input("Digite um número compreendido entre 1 e 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido")
