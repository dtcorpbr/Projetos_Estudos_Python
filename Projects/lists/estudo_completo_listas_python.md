# 🧠 Estudo Completo: Operações com Listas em Python

---

## 📘 1. O que é uma lista?

Uma **lista** é uma **estrutura de dados mutável**, **ordenada** e **iterável** que pode armazenar **valores de qualquer tipo** (números, strings, outras listas, objetos etc.).

```python
lista = [10, "Python", 3.14, True, [1, 2, 3]]
```

---

## 🧩 2. Criação de listas

| Método | Descrição | Exemplo |
|--------|------------|---------|
| `[]` | Criação literal | `lista = [1, 2, 3]` |
| `list()` | Cria a partir de um iterável | `lista = list("Python")` → `['P','y','t','h','o','n']` |
| Compreensão de lista | Gera listas dinamicamente | `[x**2 for x in range(5)]` → `[0,1,4,9,16]` |

---

## 🔍 3. Acesso a elementos

```python
lista = ['a', 'b', 'c', 'd']

print(lista[0])   # Primeiro elemento → 'a'
print(lista[-1])  # Último elemento → 'd'
print(lista[1:3]) # Fatiamento → ['b', 'c']
```

🧠 **Observação:**  
`lista[início:fim:passo]`

---

## ✏️ 4. Alteração de elementos

```python
lista = [10, 20, 30]
lista[1] = 99
print(lista)  # [10, 99, 30]

lista[0:2] = [1, 2, 3]
print(lista)  # [1, 2, 3, 30]
```

---

## ➕ 5. Adição de elementos

| Método | Função | Exemplo |
|--------|---------|----------|
| `append()` | Adiciona **um** item ao final | `lista.append(4)` |
| `extend()` | Adiciona **vários** itens | `lista.extend([5, 6])` |
| `insert()` | Adiciona em uma **posição específica** | `lista.insert(1, 99)` |

```python
lista = [1, 2, 3]
lista.append(4)
lista.extend([5, 6])
lista.insert(0, 0)
```

---

## ➖ 6. Remoção de elementos

| Método | Descrição | Exemplo |
|--------|------------|---------|
| `remove(valor)` | Remove a **primeira ocorrência** | `lista.remove(3)` |
| `pop([índice])` | Remove e **retorna** um item (por índice) | `lista.pop(2)` |
| `del lista[i]` | Remove um item por índice | `del lista[0]` |
| `clear()` | Esvazia a lista | `lista.clear()` |

---

## 📏 7. Tamanho e contagem

```python
lista = [1, 2, 3, 3, 4]
print(len(lista))   # 5
print(lista.count(3))  # 2
```

---

## 🔄 8. Ordenação e reversão

| Método | Descrição | Exemplo |
|--------|------------|---------|
| `sort()` | Ordena **a própria lista** | `lista.sort()` |
| `sorted(lista)` | Retorna uma **nova lista ordenada** | `sorted(lista)` |
| `reverse()` | Inverte a ordem | `lista.reverse()` |
| `reversed(lista)` | Retorna um **iterador invertido** | `list(reversed(lista))` |

```python
nums = [4, 1, 3, 2]
nums.sort()
nums.sort(reverse=True)
```

---

## 🧮 9. Operações matemáticas

```python
nums = [1, 2, 3, 4, 5]
print(sum(nums))   # 15
print(max(nums))   # 5
print(min(nums))   # 1
```

---

## 🔗 10. Concatenação e repetição

```python
a = [1, 2]
b = [3, 4]

print(a + b)   # [1,2,3,4]
print(a * 3)   # [1,2,1,2,1,2]
```

---

## 🧠 11. Teste de pertencimento

```python
lista = ['a', 'b', 'c']
print('a' in lista)      # True
print('z' not in lista)  # True
```

---

## 🧰 12. Cópia de listas

```python
lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista3 = lista1[:]

import copy
lista4 = copy.deepcopy(lista1)
```

---

## 🧱 13. Iteração sobre listas

```python
lista = [10, 20, 30]
for item in lista:
    print(item)

for i, valor in enumerate(lista):
    print(i, valor)
```

---

## 🧮 14. Compreensões de lista (List Comprehensions)

```python
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
matriz = [[i*j for j in range(3)] for i in range(3)]
```

---

## 🧩 15. Listas aninhadas

```python
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(matriz[1][2])  # 6

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
```

---

## ⚙️ 16. Funções e métodos úteis

| Função / Método | Descrição |
|-----------------|------------|
| `any(lista)` | `True` se **algum** elemento for verdadeiro |
| `all(lista)` | `True` se **todos** forem verdadeiros |
| `zip(lista1, lista2)` | Combina elementos em pares |
| `map(func, lista)` | Aplica uma função a todos os elementos |
| `filter(func, lista)` | Filtra elementos conforme condição |

```python
nums = [1, 2, 3, 4]
print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x%2==0, nums)))
```

---

## 🧩 17. Conversão entre tipos

```python
texto = "Python"
lista = list(texto)
tupla = tuple(lista)
```

---

## 🧼 18. Desempacotamento de listas

```python
dados = [1, 2, 3]
a, b, c = dados
print(a, b, c)

a, *b = [10, 20, 30, 40]
print(a)  # 10
print(b)  # [20, 30, 40]
```

---

## 🧠 19. Operações avançadas

```python
resultado = [x*2 for x in range(10) if x%3 == 0]

dados = [("A", 10), ("B", 5), ("C", 8)]
ordenado = sorted(dados, key=lambda x: x[1], reverse=True)
```

---

## 📚 20. Resumo dos principais métodos

| Método | Descrição |
|---------|------------|
| `append(x)` | Adiciona um elemento ao final |
| `extend(iterável)` | Adiciona todos os itens de um iterável |
| `insert(i, x)` | Insere em uma posição específica |
| `remove(x)` | Remove a primeira ocorrência |
| `pop([i])` | Remove e retorna o elemento |
| `clear()` | Remove todos os itens |
| `index(x)` | Retorna o índice da primeira ocorrência |
| `count(x)` | Conta quantas vezes aparece |
| `sort(key=None, reverse=False)` | Ordena os elementos |
| `reverse()` | Inverte a ordem |
| `copy()` | Retorna uma cópia rasa da lista |

---

## 🧾 Exemplo final integrando tudo

```python
# Criação
numeros = [5, 2, 9, 1]

# Adição
numeros.append(7)
numeros.insert(2, 3)

# Remoção
numeros.remove(9)
valor_removido = numeros.pop()

# Ordenação
numeros.sort()

# Iteração
for i, v in enumerate(numeros):
    print(f"Posição {i}: {v}")

# Compreensão
pares = [x for x in range(10) if x % 2 == 0]

# Exibição final
print("Números:", numeros)
print("Pares:", pares)
```

---
