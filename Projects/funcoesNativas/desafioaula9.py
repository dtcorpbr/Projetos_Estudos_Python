'''
Estude cada uma das funções nativas do Python e crie um pequeno programa que utilize pelo menos 5 dessas funções.
As funções nativas do Python podem ser encontradas na documentação oficial: https://docs.python.org/3/library/functions.html | ./funcoesNativas/funcoes_nativas_python.md
'''

# Exemplo: Processar uma lista de números com várias funções nativas Python

numeros = [1, -2, 3, -4, 5]

# 1. Aplicar valor absoluto (abs) e elevar ao quadrado (pow)
processados = list(map(lambda x: pow(abs(x), 2), numeros))

# 2. Filtrar apenas os pares (filter)
pares = list(filter(lambda x: x % 2 == 0, processados))

# 3. Somar os valores (sum) e calcular média
total = sum(processados)
media = total / len(processados)

# 4. Exibir resultados formatados (print, format)
print(f"Números originais: {numeros}")
print(f"Processados: {processados}")
print(f"Pares: {pares}")
print(f"Soma total: {total}, Média: {round(media, 2)}")

# 5. Mostrar maior e menor (max, min)
print("Maior valor:", max(processados))
print("Menor valor:", min(processados))

# 6. Usando zip e enumerate
nomes = ["A", "B", "C", "D", "E"]
for indice, (nome, valor) in enumerate(zip(nomes, processados)):
    print(f"{indice}: {nome} → {valor}")

# 7. Mostrar dicionário com informações (dict, vars)
dados = dict(zip(nomes, processados))
print("Dicionário criado:", dados)
print("Tipo de dados:", type(dados))
