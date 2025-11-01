nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7.0:
    print(f"{nome}, sua média foi {media:.2f}. Você está aprovado.")
elif media >= 4.0 and media < 7.0:
    print(f"{nome}, sua média foi {media:.2f}. Você está tem direito a exame.")
else:
    print(f"{nome}, sua média foi {media:.2f}. Você está reprovado.")
