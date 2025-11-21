# 🐍 Estudo Básico: Operações com Strings em Python

As **strings** em Python são sequências imutáveis de caracteres usadas
para armazenar e manipular texto.\
A seguir, apresentamos as principais operações que podem ser realizadas
com strings, acompanhadas de exemplos práticos.

------------------------------------------------------------------------

## 1. Criação de Strings

``` python
texto1 = 'Olá, mundo!'
texto2 = "Python é incrível!"
texto3 = '''Texto
com múltiplas
linhas'''
```

------------------------------------------------------------------------

## 2. Indexação e Fatiamento

Permite acessar partes específicas da string.

``` python
frase = "Python"

print(frase[0])    # P (primeiro caractere)
print(frase[-1])   # n (último caractere)
print(frase[0:3])  # Pyt (fatiamento do índice 0 ao 2)
print(frase[::2])  # Pto (pula de 2 em 2 caracteres)
```

------------------------------------------------------------------------

## 3. Concatenação e Repetição

``` python
a = "Olá"
b = "Mundo"

print(a + " " + b)   # Olá Mundo
print(a * 3)         # OláOláOlá
```

------------------------------------------------------------------------

## 4. Verificação de Substrings

``` python
frase = "Aprendendo Python"

print("Python" in frase)     # True
print("Java" not in frase)   # True
```

------------------------------------------------------------------------

## 5. Comprimento da String

``` python
texto = "Programar é divertido"
print(len(texto))  # 21
```

------------------------------------------------------------------------

## 6. Métodos de Transformação de Texto

  -----------------------------------------------------------------------------------
  Método              Descrição                     Exemplo
  ------------------- ----------------------------- ---------------------------------
  `upper()`           Converte para maiúsculas      `"python".upper()` → `"PYTHON"`

  `lower()`           Converte para minúsculas      `"PYTHON".lower()` → `"python"`

  `title()`           Primeira letra maiúscula em   `"curso de python".title()` →
                      cada palavra                  `"Curso De Python"`

  `capitalize()`      Primeira letra maiúscula,     `"python é ótimo".capitalize()` →
                      resto minúsculo               `"Python é ótimo"`

  `swapcase()`        Inverte maiúsculas/minúsculas `"PyThOn".swapcase()` →
                                                    `"pYtHoN"`
  -----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 7. Remoção de Espaços

``` python
texto = "   Python   "
print(texto.strip())   # Remove dos dois lados
print(texto.lstrip())  # Remove à esquerda
print(texto.rstrip())  # Remove à direita
```

------------------------------------------------------------------------

## 8. Substituição e Divisão

``` python
texto = "Eu gosto de Java"

# Substituir
novo_texto = texto.replace("Java", "Python")
print(novo_texto)  # Eu gosto de Python

# Dividir
palavras = novo_texto.split()
print(palavras)  # ['Eu', 'gosto', 'de', 'Python']
```

------------------------------------------------------------------------

## 9. Junção de Strings

``` python
palavras = ['Aprender', 'Python', 'é', 'legal']
frase = " ".join(palavras)
print(frase)  # Aprender Python é legal
```

------------------------------------------------------------------------

## 10. Busca e Verificação

  --------------------------------------------------------------------------------
  Método                Função                Exemplo
  --------------------- --------------------- ------------------------------------
  `startswith(sub)`     Verifica se começa    `"Python".startswith("Py") → True`
                        com `sub`             

  `endswith(sub)`       Verifica se termina   `"Python".endswith("on") → True`
                        com `sub`             

  `find(sub)`           Retorna índice da     `"Python".find("t") → 2`
                        primeira ocorrência   

  `rfind(sub)`          Retorna índice da     `"Python".rfind("o") → 4`
                        última ocorrência     

  `count(sub)`          Conta quantas vezes   `"banana".count("a") → 3`
                        `sub` aparece         
  --------------------------------------------------------------------------------

------------------------------------------------------------------------

## 11. Verificações de Tipo de Texto

  Método        Descrição           Exemplo
  ------------- ------------------- ----------------------------------------
  `isalpha()`   Apenas letras       `"Python".isalpha()` → `True`
  `isdigit()`   Apenas dígitos      `"123".isdigit()` → `True`
  `isalnum()`   Letras ou dígitos   `"abc123".isalnum()` → `True`
  `isspace()`   Apenas espaços      `"   ".isspace()` → `True`
  `islower()`   Todas minúsculas    `"python".islower()` → `True`
  `isupper()`   Todas maiúsculas    `"PYTHON".isupper()` → `True`
  `istitle()`   Estilo título       `"Curso De Python".istitle()` → `True`

------------------------------------------------------------------------

## 12. Formatação de Strings

### Usando f-strings (Python 3.6+)

``` python
nome = "Ana"
idade = 25
print(f"{nome} tem {idade} anos.")  # Ana tem 25 anos.
```

### Usando `.format()`

``` python
print("O número {0} é maior que {1}".format(10, 5))
```

### Usando `%` (modo antigo)

``` python
print("A nota é %.2f" % 9.456)  # A nota é 9.46
```

------------------------------------------------------------------------

## 13. Inversão de Strings

``` python
texto = "Python"
print(texto[::-1])  # nohtyP
```

------------------------------------------------------------------------

## 14. Caracteres Especiais e Escape

  Código   Significado       Exemplo
  -------- ----------------- ---------------------------------------------------
  `\n`     Nova linha        `"Olá\nMundo"` → Olá`<br>`{=html}Mundo
  `\t`     Tabulação         `"Python\tRocks"` → Python Rocks
  `\\`     Barra invertida   `"C:\\User\\Docs"` → C:`\User`{=tex}`\Docs`{=tex}
  `\'`     Aspa simples      `'It\'s nice' → It's nice`
  `\"`     Aspa dupla        `"Ele disse: \"Oi\""` → Ele disse: "Oi"

------------------------------------------------------------------------

## 15. Conversão para Lista de Caracteres

``` python
texto = "Python"
lista = list(texto)
print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']
```

------------------------------------------------------------------------

## 16. Comparação de Strings

``` python
print("abc" == "abc")   # True
print("abc" < "abd")    # True (ordem alfabética)
print("a" > "Z")        # True (case sensitive)
```

------------------------------------------------------------------------

# ✅ Conclusão

As operações com strings em Python são poderosas e abrangentes,
permitindo desde manipulações simples até formatações complexas de
texto.\
Dominar essas operações é fundamental para trabalhar com entrada e saída
de dados, análise textual e construção de interfaces interativas.
