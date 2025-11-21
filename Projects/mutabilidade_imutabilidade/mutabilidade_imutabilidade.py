'''
Como funciona a memória com Python?
***********************************

- Em Python, a "alocação de memória" para variáveis é toda "controlada" pelo sistema de "runtime" (interpretador).
 * Impactos na forma como dados podem (ou não) mudar na memória, em tempo de execução.

Objetos mutáveis
****************

- Uma vez que a memória foi alocada, o "estado pode ser alterado"
 * Pode "modificar" o "conteúdo sem" ter de "criar" um "novo objeto" em memória para isso.
- Listas, dicionários, conjuntos, classes definidas pelo usuário.

Objetos imutáveis
*****************

- Uma vez que a memória foi alocada, o "conteúdo fica imutável naquela região" de memória.
 * Para "alterar" o "conteúdo, só destruindo o objeto" e criando um novo.
- Strings, números e tuplas.

Funções: impactos da mutabilidade
*********************************

- Objetos "imutáveis":
 * Quando passados como argumento a funções "nãp invadem o escopo" do argumento original.
- Objetos "mutáveis":
 * Alterar o argumento, dentro da função, "implica" em "alterar" o "argumento fora do escopo" da função.

Cópia: impactos da mutabilidade
*******************************

- Objetos "mutáveis": "atribuição não cria" uma "nova cópia", apenas um 'alias'
 * Para realizar uma cópia real de um objeto, obriga-se a utilização de funções copy().
- Objetos "imutáveis": "atribuição gera cópia", sem maiores necessidades para tal.
'''
'''
Crie um programa para verificar a imutabilidade de variáveis simples numéricas e a mutabilidade de listas.
1. Crie uma variável simples e atribua o conteúdo 5 a ela. Em seguida, imprima o conteúdo e o id() da variável. Depois, altere o conteúdo da variável para 10 e imprima novamente o conteúdo e o id() da variável.

2. Crie uma lista com os valores 10, 20 e 30. Enseguida, imprimao conteúdo e o id() da lista. Depois, adicione o elemento 40 ao fim da lista e altere o conteúdo do primeiro elemento para 0. Imprima novamente o conteúdo e o id() da variável.
'''
var_num = 5

print()
print("Variável numérica (antes da alteração): ")
print("Conteúdo: ", var_num)
print("ID: ", id(var_num))

var_num = 10

print()
print("Variável numérica (depois da alteração): ")
print("Conteúdo:", var_num)
print("ID: ", id(var_num))

lista_mutavel = [10, 20, 30]

print()
print("Lista mutável (antes da alteração): ")
print("Conteúdo: ", lista_mutavel)
print("ID: ", id(lista_mutavel))

lista_mutavel.append(40)
lista_mutavel[0] = 0

print()
print("Lista mutável (depois da alteração): ")
print("Conteúdo: ", lista_mutavel)
print("ID: ", id(lista_mutavel))
