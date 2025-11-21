'''
Crie um programa com dois conjuntos (sets) de strings. O primeiro conjunto deve ser inicializado com os nomes das seguintes pessoas: "Carlos", "Josiel", "Jandira" e "Aline". O segundo grupo, deve ser "Aline", Carlos", "Jaqueline" e "Altair".
Assim sendo, descubra:
* Quais são as pessoas que estão presentes nos dois grupos?
* Quais são as pessoas que estão apenas no um grupo?
* Liste todas as pessoas mensionadas no enunciado, sem repetir seus nomes.
'''

group_1 = {"Carlos", "Josiel", "Jandira", "Aline"}
group_2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

# Quais são as pessoas que estão presentes nos dois grupos?
intersec = group_1.intersection(group_2)
print("Os nomes que aparecem nos dois grupos são: ", intersec)

# Quais são as pessoas que estão apenas em um grupo?
diferenca = group_1.symmetric_difference(group_2)
print("As pessoas que aparecem em apenas 1 grupo são: ", diferenca)

# Liste todas as pessoas mensionadas no enunciado, sem repetir seus nomes.
uniao = group_1.union(group_2)
print("Lista de pessoas nos 2 grupos são: ", uniao)

