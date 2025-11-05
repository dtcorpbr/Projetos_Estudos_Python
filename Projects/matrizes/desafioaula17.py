'''
Crie um programa que peça para o usuário digitar valores numéricos inteiros para preencher uma matriz 3x4. Após inseridos os dados, realize uma busca na matriz e informe quais são os valores das linhas e colunas (posição) do maior e do menos elemento de toda a matriz.
'''
matriz = []
for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)
for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)
print(f"O maior valor é {maior} na posição {pos_maior}")
print(f"O menor valor é {menor} na posição {pos_menor}")