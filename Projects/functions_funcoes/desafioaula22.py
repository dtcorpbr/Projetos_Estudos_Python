'''
Crie um programa para simular uma calculadora. O programa deve ter quatro funções que sejam capazes de processar a soma. Crie um menu de opções para que o usuário possa escolher qual operação matemática deseja executar.
'''

def calc():
    print("===== Calculadora Simples =====")
    print("Operações disponíveis:")
    print()
    print("===============================")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print()
    print("===============================")


calc()

print()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print()
operacao = input("Escolha a operação (+, -, *, /): ")

print()

if operacao == '+':
    result = num1 + num2
    print(f"Resultado: {num1} + {num2} = {result}")

elif operacao == '-':
    result = num1 - num2
    print(f"Resutado: {num1} - {num2} = {result}")

elif operacao == '*':
    result = num1 * num2
    print(f"Resultado: {num1} * {num2} = {result}")

elif operacao == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Resultado: {num1} / {num2} = {result}")
    else:
        print ("Erro: divisão por zero não é permitida!")
else:
    print("Operação inválida. Tente novamente.")