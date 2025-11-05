'''
Desenvolva um programa para testar suas habilidades com strings. Crie um programa que continue pedindo para que o usuário informe várias palavras. Concatene as palavras digitadas, separando-as por espaços. Quando o usuário digitar "/exit", o programa deve parar de ler as palavras (o "/exit" não deve ser incluído na concatenação). Mostre o resultado da concatenação ao final.
'''
palavras = []
while True:
    palavra = input("Digite uma palavra (ou '/exit' para sair): ")
    if palavra == "/exit":
        break
    palavras.append(palavra)
resultado = " ".join(palavras)
print("Palavras concatenadas:", resultado)