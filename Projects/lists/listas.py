'''
Declare uma lista vazia. Em seguida, solicite ao usuário que informe os 5 (cinco) elementos que serão armazenados na lista - utilize o append(). Calcule a média entre os elementos da lista e mostre o resultado na tela. Imprima o conteúdo de cada um dos elementos da lista, individualmente, na tela. 
'''
v = []
s = 0

for i in range(5):
    dado = int(input("Informe um número: "))
    v.append(dado)
    s += dado

media = s / 5

for elem in v:
    print(elem, end=" ")

print(f"Média dos elementos: {media}")