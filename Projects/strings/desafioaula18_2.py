'''
Pesquise sobre o funcionamento de cada uma das operações listadas, sobre strings.

O arquivo em Markdown a seguir contém um estudo básico sobre operações com strings em Python. Esta em /Projects/strings/Operacoes_Strings_Python.md
'''
# ============================================
# 🐍 ESTUDO BÁSICO: OPERAÇÕES COM STRINGS EM PYTHON
# ============================================

# 1. Criação de Strings
texto1 = 'Olá, mundo!'
texto2 = "Python é incrível!"
texto3 = '''Texto
com múltiplas
linhas'''

print(texto1)
print(texto2)
print(texto3)

# 2. Indexação e Fatiamento
frase = "Python"
print(frase[0])     # P
print(frase[-1])    # n
print(frase[0:3])   # Pyt
print(frase[::2])   # Pto

# 3. Concatenação e Repetição
a = "Olá"
b = "Mundo"
print(a + " " + b)  # Olá Mundo
print(a * 3)        # OláOláOlá

# 4. Verificação de Substrings
frase = "Aprendendo Python"
print("Python" in frase)    # True
print("Java" not in frase)  # True

# 5. Comprimento da String
texto = "Programar é divertido"
print(len(texto))  # 21

# 6. Métodos de Transformação de Texto
print("python".upper())        # PYTHON
print("PYTHON".lower())        # python
print("curso de python".title())   # Curso De Python
print("python é ótimo".capitalize())  # Python é ótimo
print("PyThOn".swapcase())     # pYtHoN

# 7. Remoção de Espaços
texto = "   Python   "
print(texto.strip())   # Remove dos dois lados
print(texto.lstrip())  # Remove à esquerda
print(texto.rstrip())  # Remove à direita

# 8. Substituição e Divisão
texto = "Eu gosto de Java"
novo_texto = texto.replace("Java", "Python")
print(novo_texto)  # Eu gosto de Python
palavras = novo_texto.split()
print(palavras)    # ['Eu', 'gosto', 'de', 'Python']

# 9. Junção de Strings
palavras = ['Aprender', 'Python', 'é', 'legal']
frase = " ".join(palavras)
print(frase)  # Aprender Python é legal

# 10. Busca e Verificação
print("Python".startswith("Py"))   # True
print("Python".endswith("on"))     # True
print("Python".find("t"))          # 2
print("Python".rfind("o"))         # 4
print("banana".count("a"))         # 3

# 11. Verificações de Tipo de Texto
print("Python".isalpha())    # True
print("123".isdigit())       # True
print("abc123".isalnum())    # True
print("   ".isspace())       # True
print("python".islower())    # True
print("PYTHON".isupper())    # True
print("Curso De Python".istitle())  # True

# 12. Formatação de Strings
nome = "Ana"
idade = 25
print(f"{nome} tem {idade} anos.")  # Ana tem 25 anos.
print("O número {0} é maior que {1}".format(10, 5))
print("A nota é %.2f" % 9.456)

# 13. Inversão de Strings
texto = "Python"
print(texto[::-1])  # nohtyP

# 14. Caracteres Especiais e Escape
print("Olá\nMundo")     # Nova linha
print("Python\tRocks")  # Tabulação
print("C:\\User\\Docs")  # Barra invertida
print('It\'s nice')     # Aspa simples
print("Ele disse: \"Oi\"")  # Aspa dupla

# 15. Conversão para Lista de Caracteres
texto = "Python"
lista = list(texto)
print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']

# 16. Comparação de Strings
print("abc" == "abc")   # True
print("abc" < "abd")    # True
print("a" > "Z")        # True (case sensitive)

# ============================================
# ✅ Fim do estudo
# ============================================
