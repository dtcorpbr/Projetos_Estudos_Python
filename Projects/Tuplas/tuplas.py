'''
Tuplas

- Similar a listas
 * Parênteses ao invés de colchetes
- Coleção de elementos
 * A ordem importa
 * Imutável (não pode ser alterada após a criação)
 * Pode conter elementos de tipos distintos

 Sintaxe:
    tupla = (elemento1, elemento2, elemento3)
    Exemplo:
    tupla = (1, "texto", 3.14, True)
 Sintaxe para acessar o elemento:
    tupla[indice]
    Exemplo:
    tupla = (1, "texto", 3.14, True)
    print(tupla[1])  # Saída: texto
- Operações comuns:
 * len(tupla): Retorna o número de elementos na tupla
 * count(valor): Conta quantas vezes um valor aparece na tupla
 * index(valor): Retorna o índice da primeira ocorrência de um valor na tupla
'''
'''
Declare uma tupla com os valores 0,1,3,3,5,7,7 e 7. Imprima, na tela, o conteúdo da tupla, a quantidade de elementos e também quantos elementos iguais a 7 estão na tupla. Imprima o elemento presente na posição 4 da tupla (quinta posição).
'''
tupla = (0, 1, 3, 3, 5, 7, 7, 7)

print("Conteúdo da tupla: ", tupla)

qtde_elems = len(tupla)
print("Quantidade de elementos na tupla: ", qtde_elems)

qtde_elems_7 = tupla.count(7)
print("Quantidade de elementos iguais a 7 na tupla: ", qtde_elems_7)

elem_pos_4 = tupla[4]
print("Elemento na posição 4 da tupla: ", elem_pos_4)