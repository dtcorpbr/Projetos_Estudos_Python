'''
Crie uma lista denominada mat. Adicione outras três sub-listas a mat, cada uma delas com os respectivos elementos

I. Sub-lista 1: 1, 2, 3
II. Sub-lista 2: 4, 5, 6
III. Sub-lista 3: 7, 8, 9

- Imprima todos os elementos da primeira linha, utilizando mat, dentro de um laço.
- Imprima todos os elementos numéricos armazenados em mat, dentro de um laço.
'''
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elementos da primeira linha:")
for elemento in mat[0]:
    print(elemento, end=' ')

print()  # Para pular uma linha entre as saídas

print("Todos os elementos da matriz:")
for linha in mat:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Para pular uma linha após cada linha da matriz