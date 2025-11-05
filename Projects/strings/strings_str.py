'''
Strings <str> - Tipo de dado string
Definição: Conjunto de caracteres delimitados por aspas simples ou duplas.

Operações comuns:
- Concatenação: junte strings com o operador +. <str1> + <str2>
- Repetição: repita strings com o operador *. <str> * <n>
- Indexação: acesse caracteres individuais usando colchetes []. <str>[<índice>]
- Pertencimento: verifique se uma substring está presente com o operador in. <substring> in <str>
- Igualdade: compare strings com os operadores == e !=. <str1> == <str2>, <str1> != <str2>
- Fatiamento (slicing): extraia substrings usando a notação [início:fim:passo]. <str>[<início>:<fim>:<passo>]

str: operações:
upper()         - Converte todos os caracteres para maiúsculas.
lower()         - Converte todos os caracteres para minúsculas.
strip()         - Remove espaços em branco do início e do fim da string.
lstrip()        - Remove espaços em branco do início da string.
rstrip()        - Remove espaços em branco do fim da string.
replace(old, new) - Substitui todas as ocorrências de 'old' por 'new'.
split(sep=None)  - Divide a string em uma lista de substrings com base no separador 'sep'.
join(iterable)   - Junta uma lista de strings em uma única string, usando a string atual como separador.
startswith(prefix) - Verifica se a string começa com o prefixo especificado.
endswith(suffix)   - Verifica se a string termina com o sufixo especific
find(sub)     - Retorna o índice da primeira ocorrência de 'sub' ou -1 se não for encontrado.
count(sub)    - Conta o número de ocorrências de 'sub' na string.
isalpha()    - Verifica se todos os caracteres são alfabéticos.
isdigit()    - Verifica se todos os caracteres são dígitos.
isalnum()    - Verifica se todos os caracteres são alfanuméricos.
isnumeric()  - Verifica se todos os caracteres são numéricos.
'''
nome = input("Qual é o seu nome? ")
sobrenome = input("Qual é o seu sobrenome? ")

comp_nome = len(nome)
comp_sobrenome = len(sobrenome)

nome_completo = nome + " " + sobrenome

comp_nome_completo = len(nome_completo)

print(f"Comprimento do nome: {comp_nome}")
print(f"Comprimento do sobrenome: {comp_sobrenome}")

print(f"Seu nome é {nome} {sobrenome}")
print(f"Comprimento do nome completo: {comp_nome_completo}")