'''
Funções (functions)
-------------------
 - Para resolver problemas complexos, é preciso "resolver problemas" mais "simples"
  * Funções para resolver problemas menores, mais simples e "geralmente recorrentes"
 - Separação de responsabilidades
 - Manutenibilidade
 
- Sintaxe de definição
----------------------
def <nome_função> (<parâmetros>):
    <corpo_da_função>
    return <retorno>
    
- Sintaxe de invocação
----------------------
<nome_função>(<argumentos>)

- Funções
 - Identificador: cuidado com as regras para nomeação
 - Parâmetro: lista de variáveis de entradas necessárias ao invocar a função
  * Pode vários, apenas um ou nenhum parâmetro
  * Pode-se definir um valor padrão
 - Retorno: pode, ou não, produzir um valor de retorno
  * Deve-se atribuir o valor a alguma variável, durante a invocação
- Funções: escopo
 - Funções definem um novo bloco de comandos: escopo
  * Variáveis locais
  * Variáveis globais
'''
#Crie um programa para definir e executar uma função que receba dois números como parâmetro e retorna o maior entre os dois números.

# def encontra_maior(A,B):
#     if A > B:
#         return A
#     else:
#         return B
    
# # invocação escopo global
# res = encontra_maior(10,20) 

# print("O maior número é: ", res)

def encontra_maior(A,B):
    if A > B:
        return A
    else:
        return B

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

res = encontra_maior(numero1, numero2)

print("O maior número é: ", res)