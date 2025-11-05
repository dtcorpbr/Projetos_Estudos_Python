name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
nationality = input("Digite sua nacionalidade: ")
wage = float(input("Digite seu salário: "))

print(
    f"Olá, eu sou {name.upper(): >8}, tenho {age} anos, sou {nationality.upper()[:2]} e ganho R$ {wage: .2f} por mês."
)
