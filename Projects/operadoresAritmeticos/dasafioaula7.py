#crie um programa que peça ao usuário para informar 3 (três) números com casas decimais.
# > Calcule a média dos 3 (três) números, e mostre o resultado na tela, formatando para apresentar apenas 2 (duas) casas decimais.

num1 = float(input("Digite o primeiro número com casas decimais: "))
num2 = float(input("Digite o segundo número com casas decimais: "))
num3 = float(input("Digite o terceiro número com casas decimais: "))

media = (num1 + num2 + num3) / 3
print("**************************************")
print(f"A média dos três números é: {media:.2f}")