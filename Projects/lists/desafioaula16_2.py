'''
Investigue cada uma das operações sobre listas.
Explique o funcionamento de cada uma delas.
'''
# Criando uma lista vazia
minha_lista = []
# Adicionando elementos à lista usando:
# append() - adiciona um único elemento ao final da lista
minha_lista.append(10)  # Adiciona o número 10 ao final da
# extend() - adiciona múltiplos elementos ao final da lista
minha_lista.extend([20, 30])  # Adiciona múltiplos elementos
# insert() - insere um elemento em uma posição específica
minha_lista.insert(1, 15)  # Insere o número 15 na posição 1

# Removendo elementos da lista usando:
# remove() - remove o primeiro elemento com o valor especificado
minha_lista.remove(20)  # Remove o número 20 da lista
# pop() - remove o elemento na posição especificada (ou o último se não for especificado)
ultimo_elemento = minha_lista.pop()  # Remove e retorna o último elemento
# del - remove o elemento na posição especificada
del minha_lista[0]  # Remove o elemento na posição 0
# clear() - remove todos os elementos da lista
minha_lista.clear()  # Limpa a lista
# tamanho da lista usando len()
tamanho = len(minha_lista)  # Obtém o tamanho da lista
print(f"Tamanho da lista: {tamanho}")

# Ordenando a lista usando:
# sort() - ordena a lista em ordem crescente
minha_lista.sort()
# reverse() - inverte a ordem dos elementos na lista
minha_lista.reverse()
# reversed() - retorna um iterador que percorre a lista em ordem reversa
minha_lista.sort(reverse=true)

# Operadoçoes matemáticas:
# sum() - retorna a soma dos elementos da lista
soma = sum(minha_lista)  # Soma dos elementos da lista
# min() - retorna o menor elemento da lista
menor = min(minha_lista)  # Menor elemento da lista
# max() - retorna o maior elemento da lista
maior = max(minha_lista)  # Maior elemento da lista

#Concatenação e repetição:
# concatenação - une duas listas
outra_lista = [40, 50]
lista_concatenada = minha_lista + outra_lista  # Concatena duas listas
# repetição - repete os elementos da lista um número específico de vezes
lista_repetida = minha_lista * 2  # Repete a lista duas vezes

# Funções e métodos úteis:
# any() - retorna True se algum elemento da lista for verdadeiro
tem_elemento_verdadeiro = any(minha_lista)
# all() - retorna True se todos os elementos da lista forem verdadeiros
todos_elementos_verdadeiros = all(minha_lista)
# zip() - combina elementos de múltiplas listas em tuplas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = list(zip(lista1, lista2))  # Combina as duas listas
# map() - aplica uma função a todos os elementos da lista
quadrados = list(map(lambda x: x**2, minha_lista))  # Eleva ao quadrado cada elemento
# filter() - filtra elementos da lista com base em uma condição
pares = list(filter(lambda x: x % 2 == 0, minha_lista))  # Filtra números pares

# Conversão entre listas e outros tipos:
# list() - converte outros tipos iteráveis em listas
tupla = (1, 2, 3)
lista_de_tupla = list(tupla)  # Converte tupla em lista
# tuple() - converte listas em tuplas
tupla_de_lista = tuple(minha_lista)  # Converte lista em tupla

'''
Conteúdo completo no arquivo: Projetos_Estudos_Python/Projects/lists/estudo_completo_listas_python.md
'''