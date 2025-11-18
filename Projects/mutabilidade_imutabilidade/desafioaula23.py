'''
Escreva um resumo do que você aprendeu sobre mutabilidade e imutabilidade, para que você fixe os conceitos aprendidos aqui.

1. Crie uma função e imprima seu conteúdo e imprima o id(), depois altere e imprima o conteúdo e o id().
2. Crie uma função lista dentro e fora da função e imprima os conteúdos dentro e fora da função com os id().
'''
def funcao_imutavel(x):
    print("Dentro da função (antes da alteração): ")
    print("Conteúdo: ", x)
    print("ID: ", id(x))
    
    x = x + 5
    
    print("Dentro da função (depois da alteração): ")
    print("Conteúdo: ", x)
    print("ID: ", id(x))
var_imutavel = 10
print("Fora da função (antes da invocação): ")
print("Conteúdo: ", var_imutavel)
print("ID: ", id(var_imutavel))
funcao_imutavel(var_imutavel)
print("Fora da função (depois da invocação): ")
print("Conteúdo: ", var_imutavel)
print("ID: ", id(var_imutavel))
def funcao_mutavel(lista):
    print("Dentro da função (antes da alteração): ")
    print("Conteúdo: ", lista)
    print("ID: ", id(lista))
    
    lista.append(4)
    lista[0] = 0
    
    print("Dentro da função (depois da alteração): ")
    print("Conteúdo: ", lista)
    print("ID: ", id(lista))
lista_mutavel = [1, 2, 3]
print("Fora da função (antes da invocação): ")
print("Conteúdo: ", lista_mutavel)
print("ID: ", id(lista_mutavel))
funcao_mutavel(lista_mutavel)
print("Fora da função (depois da invocação): ")
print("Conteúdo: ", lista_mutavel)
print("ID: ", id(lista_mutavel))
'''
Mutabilidade e Imutabilidade
***************************
Objetos mutáveis
*****************
- O "conteúdo pode ser modificado" sem que seja necessário "criar um novo objeto" em memória.
 * Alterações são feitas na mesma região de memória.
 - Exemplos: listas, dicionários, conjuntos, classes definidas pelo usuário.
 
 Objetos imutáveis
 *****************
 - O "conteúdo não pode ser modificado" na mesma região de memória.
 * Para "alterar o conteúdo", é necessário "criar um novo objeto" em memória.
 - Exemplos: strings, números e tuplas.
 
 Funções: impactos da mutabilidade
 *********************************
 - Objetos "imutáveis":
  * Quando passados como argumento a funções, "não alteram o valor" do argumento original fora da função.
  - Objetos "mutáveis":
  * Alterações feitas no argumento dentro da função "afetam o argumento" fora da função.
  
  Cópia: impactos da mutabilidade
  *******************************
  - Objetos "mutáveis": "atribuição cria um alias", ou seja, não cria uma nova cópia do objeto.
  * Para criar uma cópia real de um objeto mutável, é necessário utilizar funções como copy().
  - Objetos "imutáveis": "atribuição cria uma nova cópia" do objeto, sem necessidade de funções adicionais.
  '''