# 🐍 Palavras Reservadas do Python – Explicação e Exemplos

As **palavras reservadas** são termos especiais usados pela linguagem Python. Elas **não podem ser utilizadas como nomes de variáveis, funções ou identificadores**, pois possuem significado próprio para o interpretador.

---

## 🔹 Valores e Lógicos

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `True` | Valor booleano verdadeiro. | `ativo = True` |
| `False` | Valor booleano falso. | `ativo = False` |
| `None` | Representa ausência de valor. | `valor = None` |
| `and` | Operador lógico "E". | `if x > 0 and y > 0:` |
| `or` | Operador lógico "OU". | `if a == 1 or b == 2:` |
| `not` | Negação lógica. | `if not ativo:` |
| `is` | Compara se dois objetos são o mesmo. | `a is b` |
| `in` | Verifica presença em sequência. | `'a' in 'casa'` |

---

## 🔹 Controle de Fluxo

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `if` | Testa uma condição. | `if x > 10: print("Maior")` |
| `elif` | Condição alternativa. | `elif x == 10:` |
| `else` | Executa se todas as anteriores forem falsas. | `else: print("Menor")` |
| `for` | Loop sobre sequência. | `for i in range(3): print(i)` |
| `while` | Loop enquanto condição for verdadeira. | `while x < 5: x += 1` |
| `break` | Encerra o loop atual. | `if i == 3: break` |
| `continue` | Pula para próxima iteração. | `if i == 2: continue` |
| `pass` | Faz nada (placeholder). | `if cond: pass` |

---

## 🔹 Funções e Escopo

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `def` | Define uma função. | `def soma(a,b): return a+b` |
| `return` | Retorna valor de função. | `return resultado` |
| `lambda` | Cria função anônima. | `dobro = lambda x: x*2` |
| `global` | Usa variável global dentro da função. | `global contador` |
| `nonlocal` | Usa variável do escopo superior (não global). | `nonlocal valor` |

---

## 🔹 Classes e Objetos

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `class` | Cria uma classe. | `class Pessoa: pass` |
| `del` | Remove variável ou atributo. | `del lista[0]` |

---

## 🔹 Tratamento de Exceções

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `try` | Testa bloco que pode gerar erro. | `try: x = 1/0` |
| `except` | Captura exceção. | `except ZeroDivisionError:` |
| `finally` | Executa sempre, com ou sem erro. | `finally: print("Fim")` |
| `raise` | Lança uma exceção. | `raise ValueError("Erro!")` |
| `assert` | Verifica condição; lança erro se falsa. | `assert x > 0` |

---

## 🔹 Módulos e Importação

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `import` | Importa módulo. | `import math` |
| `from` | Importa parte específica. | `from math import sqrt` |
| `as` | Define apelido para módulo. | `import numpy as np` |

---

## 🔹 Programação Assíncrona e Geradores

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `async` | Define função assíncrona. | `async def tarefa(): await asyncio.sleep(1)` |
| `await` | Espera resultado de função assíncrona. | `await tarefa()` |
| `yield` | Retorna valor de um gerador. | `yield i` |

---

## 🔹 Contexto e Estruturas Especiais

| Palavra | Descrição | Exemplo |
|----------|------------|---------|
| `with` | Gerencia contexto automaticamente. | `with open('arquivo.txt') as f:` |
| `match` | Estrutura de correspondência (switch-case). | `match cor: case "azul": print("ok")` |
| `case` | Define um caso dentro do match. | `case "vermelho": print("alerta")` |

---

## 💡 Dica Final

Para listar todas as palavras reservadas da sua versão do Python:

```python
import keyword
print(keyword.kwlist)
```

---

> Arquivo gerado automaticamente por ChatGPT – Referência rápida para estudo de Python 🚀
