# Estudo — Operações sobre Dicionários em Python

> Documento contém explicações e exemplos de código sobre todas as principais operações com `dict` em Python. Inclui também exemplos práticos e um arquivo de código para executar.

---

## Sumário

1. O que é um dicionário
2. Criação de dicionários
3. Acesso a valores
4. Adição e atualização
5. Remoção de itens
6. Métodos de consulta (keys, values, items, get, setdefault)
7. União / mesclagem
8. Cópias e views
9. Iteração
10. Operações úteis (len, in, clear, fromkeys, comprehension)
11. Exemplo completo de uso
12. Arquivo `exemplos_dicionarios.py`

---

## 1. O que é um dicionário

Um `dict` é uma coleção não ordenada (desde Python 3.7 a ordem de inserção é preservada) de pares chave:valor. As chaves devem ser objetos *hashable* (imutáveis como `str`, `int`, `tuple` etc.).

Exemplo: `{'nome': 'Ana', 'idade': 30}`

---

## 2. Criação de dicionários

```python
# forma literal
d1 = {'a': 1, 'b': 2}

# construtor dict
d2 = dict(x=10, y=20)

# a partir de lista de tuplas
d3 = dict([('k1', 'v1'), ('k2', 'v2')])

# com fromkeys (cria chaves com mesmo valor)
keys = ['k1', 'k2']
d4 = dict.fromkeys(keys, 0)  # {'k1': 0, 'k2': 0}

# comprehension de dicionário
squares = {n: n*n for n in range(6)}  # {0:0, 1:1, 2:4, ...}
```

---

## 3. Acesso a valores

```python
person = {'nome': 'João', 'idade': 25}

# acesso direto (levanta KeyError se a chave não existir)
idade = person['idade']

# get (retorna None ou valor default se não existir)
profissao = person.get('profissao')  # None
profissao2 = person.get('profissao', 'Desconhecida')
```

---

## 4. Adição e atualização

```python
d = {}
# atribuição cria ou atualiza
d['novo'] = 42

# update: recebe outro dict ou iterável de pares
d.update({'outro': 99})
d.update([('a', 1), ('b', 2)])

# setdefault: retorna o valor existente ou define e retorna o default
x = d.setdefault('c', 0)  # se 'c' não existe, cria com 0 e retorna 0
```

---

## 5. Remoção de itens

```python
d = {'a': 1, 'b': 2, 'c': 3}

# pop: remove e retorna o valor; pode receber default
val = d.pop('b')          # 2
val2 = d.pop('z', None)   # None (não levanta erro)

# popitem: remove e retorna o último par inserido (Python 3.7+)
last = d.popitem()        # ('c', 3)

# del: remove por chave (levanta KeyError se não existir)
del d['a']

# clear: remove todos os itens
d.clear()
```

---

## 6. Métodos de consulta

```python
d = {'x': 1, 'y': 2}

# keys, values, items retornam *views* dinâmicas
k = d.keys()    # dict_keys(['x','y'])
v = d.values()  # dict_values([1,2])
i = d.items()   # dict_items([('x',1), ('y',2)])

# essas views refletem mudanças no dict
d['z'] = 3
print(list(k))  # ['x','y','z']

# membership
'x' in d        # True
1 in d.values() # True

# conversão para listas quando precisar manipular
a_lista = list(d.items())
```

---

## 7. União / mesclagem

```python
a = {'a': 1, 'b': 2}
b = {'b': 20, 'c': 3}

# Python 3.9+: operador |
c = a | b  # {'a':1, 'b':20, 'c':3}

# operador |= modifica in-place
a |= b     # a agora é {'a':1, 'b':20, 'c':3}

# antes do 3.9: usar {**a, **b}
d = {**a, **b}  # cria novo dict com chaves de b sobrescrevendo a

# ou update para modificar in-place
a.update(b)
```

---

## 8. Cópias e views

```python
orig = {'a': [1,2], 'b': 2}
shallow = orig.copy()          # cópia superficial (shallow)
import copy
deep = copy.deepcopy(orig)   # cópia profunda

# modificar shallow['a'].append(3) afetará orig porque lista é referenciada
```

---

## 9. Iteração

```python
d = {'x': 1, 'y': 2}
for chave in d:                # itera chaves
    print(chave, d[chave])

for k, v in d.items():         # itera pares
    print(k, v)

# iterar somente valores
for v in d.values():
    print(v)
```

---

## 10. Operações úteis e boas práticas

- `len(d)` retorna número de pares
- usar `get` quando a chave pode não existir para evitar exceções
- preferir `dict.setdefault` com cuidado (útil para agrupar valores)
- usar `collections.defaultdict(list)` quando for popular para agrupar
- ao mesclar, prefira `|` quando disponível para clareza

Exemplo de agrupamento com setdefault:

```python
pessoas = [('Ana', 'SP'), ('Bruno', 'RJ'), ('Carlos', 'SP')]
por_estado = {}
for nome, estado in pessoas:
    por_estado.setdefault(estado, []).append(nome)
# {'SP': ['Ana','Carlos'], 'RJ': ['Bruno']}
```

Exemplo com defaultdict (mais elegante):

```python
from collections import defaultdict
por_estado = defaultdict(list)
for nome, estado in pessoas:
    por_estado[estado].append(nome)
```

---

## 11. Exemplo completo de uso

```python
# pequenas funções demonstrativas

def merge_defaults(user_cfg, default_cfg):
    """Retorna um novo dicionário com valores do usuário sobrescrevendo defaults."""
    return {**default_cfg, **user_cfg}


def invert_dict(d):
    """Inverte chaves e valores. Se houver colisão, os últimos sobrescrevem."""
    return {v: k for k, v in d.items()}


if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    user = {'port': 9090}
    cfg = merge_defaults(user, defaults)
    print(cfg)
    
    d = {'a': 1, 'b': 2}
    print(invert_dict(d))
```

---

## 12. Arquivo `exemplos_dicionarios.py`

No arquivo abaixo há uma coleção de exemplos prontos para executar — copie para um arquivo `.py` e rode com `python exemplos_dicionarios.py`.

```python
"""exemplos_dicionarios.py
Coleção de pequenos exemplos demonstrando operações com dict.
"""

from collections import defaultdict
import copy


def demo_criacao():
    a = {'x': 1}
    b = dict(y=2)
    c = dict([('z', 3)])
    print('criados:', a, b, c)


def demo_acesso():
    p = {'nome': 'Maria'}
    print(p.get('idade', 'idade desconhecida'))


def demo_update_pop():
    d = {'a': 1, 'b': 2}
    d.update({'b': 20, 'c': 3})
    print('after update', d)
    print('pop b ->', d.pop('b'))


def demo_merge():
    a = {'a': 1}
    b = {'a': 10, 'b': 2}
    print('merge', a | b)


def demo_copy():
    o = {'a': [1,2]}
    s = o.copy()
    s['a'].append(3)
    print('orig', o)
    d = copy.deepcopy(o)
    d['a'].append(4)
    print('deep', o, d)


if __name__ == '__main__':
    demo_criacao()
    demo_acesso()
    demo_update_pop()
    demo_merge()
    demo_copy()
```

---

### Quer alterar o material?

Posso:
- Gerar um arquivo `.py` separado para download;
- Exportar o documento em outro formato (PDF);
- Incluir exercícios e soluções.

Se quiser eu já preparo o arquivo `.py` para baixar também — diga qual opção prefere.

