# 🧠 Estudo Completo sobre Operações de Sets em Python

Os **sets (conjuntos)** em Python são coleções **não ordenadas, mutáveis e que não permitem elementos duplicados**.  
Eles são muito úteis para operações matemáticas como **união, interseção e diferença**.

---

## 📘 1. Criando Sets

```python
# Criando um set
frutas = {"maçã", "banana", "laranja"}
print(frutas)

# Criando um set a partir de uma lista
numeros = set([1, 2, 3, 4, 5])
print(numeros)
```

---

## ➕ 2. Adicionar elementos

```python
# Adiciona um único elemento
frutas.add("uva")
print(frutas)

# Adiciona múltiplos elementos
frutas.update(["abacaxi", "melancia"])
print(frutas)
```

---

## ➖ 3. Remover elementos

```python
# Remove um elemento (erro se não existir)
frutas.remove("banana")

# Remove um elemento (sem erro se não existir)
frutas.discard("morango")

# Remove e retorna um elemento aleatório
item = frutas.pop()
print("Removido:", item)

# Limpa todos os elementos
frutas.clear()
print(frutas)
```

---

## 🔍 4. Verificar se um elemento está no set

```python
frutas = {"maçã", "banana", "uva"}
print("maçã" in frutas)    # True
print("laranja" not in frutas)  # True
```

---

## ⚖️ 5. União (`union` ou `|`)

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))  # {1, 2, 3, 4, 5}
print(A | B)       # Forma alternativa
```

---

## ⚔️ 6. Interseção (`intersection` ou `&`)

```python
A = {1, 2, 3}
B = {2, 3, 4}
print(A.intersection(B))  # {2, 3}
print(A & B)              # Forma alternativa
```

---

## ➗ 7. Diferença (`difference` ou `-`)

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
print(A.difference(B))  # {1, 2}
print(A - B)            # Forma alternativa
```

---

## 🔄 8. Diferença simétrica (`symmetric_difference` ou `^`)

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))  # {1, 2, 4, 5}
print(A ^ B)                      # Forma alternativa
```

---

## 🧩 9. Subconjunto e Superconjunto

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True  → A está contido em B
print(B.issuperset(A)) # True  → B contém A
```

---

## ⚖️ 10. Conjuntos disjuntos

```python
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))  # True → não possuem elementos em comum
```

---

## 🧮 11. Copiar sets

```python
A = {1, 2, 3}
B = A.copy()
print(B)  # {1, 2, 3}
```

---

## 🧑‍💻 Exemplo prático

```python
# Remover duplicatas de uma lista usando set
numeros = [1, 2, 2, 3, 4, 4, 5]
sem_duplicatas = list(set(numeros))
print(sem_duplicatas)  # [1, 2, 3, 4, 5]
```

---

## 📚 Conclusão

Os **sets** são extremamente úteis para:
- Eliminar duplicatas;
- Fazer operações matemáticas de conjuntos;
- Melhorar performance em verificações de pertencimento (`in`);
- Trabalhar com coleções únicas e mutáveis.

---

> 💡 **Dica:** Use sets quando precisar garantir **unicidade** dos elementos e realizar **operações de comparação** entre coleções.
