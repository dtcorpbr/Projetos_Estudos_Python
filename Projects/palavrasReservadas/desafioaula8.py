'''
Pesquise sobre o funcionamento da palavra reservada do Python, listadas anteriormente, e crie um pequeno código comentado, explicando o seu funcionamento.
'''

'''Exemplo de código que lista todas as palavras reservadas em Python.'''
import keyword
print(keyword.kwlist)

'''Valores e lógicos'''
#True -> Representa o valor booleano verdadeiro. | ativo = True
#False -> Representa o valor booleano falso | ativo = False
#None ->Representa a ausência de valor | resultado = None
#and -> Operador lógico "E" | if x > 0 and x < 10:
#or  -> Operador lógico "OU" | if x < 0 or x > 10:
#not -> Operador lógico "NÃO" | if not x == 0:
#is  -> Verifica identidade entre objetos | if a is b:
#in  -> Verifica se um valor está presente em uma sequência | if x in lista:

'''Controle de fluxo'''
#if -> Testa uma condição. | if x > 0:
#elif -> Testa uma condição alternativa. | elif x == 0:
#else -> Define uma alternativa. | else: print("menor")
#for -> Loop sobre uma sequência. | for i in range(5): print(i)
#while -> Loop baseado em uma condição verdadeira. | while x < 10: x += 1
#break -> Encerra o loop atual. | if i == 3: break
#continue -> Pula para a próxima iteração do loop. | if i % 2 == 0: continue
#pass -> Declaração nula, usada como placeholder. | def func(): pass

'''Funções e escopo'''
#def -> Define uma função. | def minha_funcao():
#return -> Retorna um valor de uma função. | return x
#lambda -> Cria funções anônimas. | f = lambda x: x * 2
#global -> Declara uma variável como global. | global x
#nonlocal -> Declara uma variável como não local. | nonlocal y

'''Calsses e Objetos'''
#class -> Define uma classe. | class MinhaClasse:
#del -> Remove um objeto. | del x

'''Tratamento de exceções'''
#try -> Inicia um bloco de código que pode gerar exceção. | try: x = 1 / 0
#except -> Define um bloco para tratar exceções. | except ZeroDivisionError:
#finally -> Define um bloco que sempre será executado. | finally: print("Fim")
#raise -> Lança uma exceção. | raise ValueError("Erro!")
#assert -> Verifica uma condição e lança uma exceção se for falsa. | assert x > 0, "x deve ser positivo"

'''Importação de módulos'''
#import -> Importa um módulo. | import math
#from -> Importa partes específicas de um módulo. | from math import sqrt
#as -> Cria um alias para um módulo importado. | import numpy as np

'''Programação assíncrona e geradores'''
#async -> Define uma função assíncrona. | async def minha_funcao():
#await -> Espera a conclusão de uma coroutine. | await minha_funcao()
#yield -> Produz um valor em um gerador. | yield x

'''Contexto e Estrutura Especiais'''
#with -> Gerencia contexto de recursos. | with open("arquivo.txt") as f:
#match -> Inicia uma estrutura de correspondência de padrões. | match x:
#case -> Define um caso dentro de uma estrutura match. | case 1: