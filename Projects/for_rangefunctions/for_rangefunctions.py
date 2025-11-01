'''
Sintaxe: range(<inicio>, <fim>, <passo>)

Semantica: produz uma sequencia numerica (iterável)
 - De <inicio> (incluindo o elemento inicial)
 - Até <fim> (excluindo o elemento final)
 - Passo a <passo>

 Comumente utilizada com o comando for.
'''
for i in range(1, 11, 1):
    print(i, " ", end="")