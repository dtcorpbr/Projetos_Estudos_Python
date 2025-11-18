'''
Sets em Python

- Similar a listas
 * Chaves ao invés de colchetes
- Coleção de elementos
 * A ordem não importa
 * Mutável
 * Não permite elementos duplicados

 - não há uma sintaxe de acesso a elementos (conjunto não ordenado)
 - Sintaxe declaração:
    <nome_do_set> = {<dados>}
'''
'''
Crie dois conjuntos: o primeiro com os valores 1, 2, 3 e 4; o segundo com os valores 3, 4, 5 e 6. Imprima os dois conjuntos na tela. Mostre na tela o resultado das operações de união, intersecção e a diferença entre os conjuntos.
'''
conj1 = {1, 2, 3, 4}
conj2 = {3, 4, 5, 6}

print("Conjunto 1: ", conj1)
print("Conjunto 2: ", conj2)

# União
uniao = conj1.union(conj2)
print("Resultado da União: ", uniao)
# Intersecção
intersecao = conj1.intersection(conj2)
print("Resultado da Intersecção: ", intersecao)
# Diferença
diferenca = conj1.difference(conj2)
print("Resultado da Diferença (conj1 - conj2): ", diferenca)