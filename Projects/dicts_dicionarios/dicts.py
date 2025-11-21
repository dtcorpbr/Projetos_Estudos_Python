'''
Dicionários (dicts)
- Também conhecidos como "dicts"
 * Armazenam arranjos de dados
- Estrutura mutável
- Ordenado
- Implementado, internamente, como uma tabela hash.

- Formato "chave-valor"
 * Para cada chave,um valor
 * Chaves devem ser únicas
  * Tipos: strings, números (inteiros ou floats), tuplas
   * Não funciona: lista, dicts, etc.
 * Valores podem ser de qualquer tipo.

- Sintaxe de declaração:
<dicts> = {
    <chave1>: <valor1>,
    <chave2>: <valor2>,
    ...
    <chaveN>: <valorN>
}

- Sintaxe de acesso:
<dict>[<chave>]
'''
'''
Modele um dicionário para representar os dados de uma pessoa que possui nome, idade e peso. Crie uma pessoa cujos dados são "Teste" para o nome, 0.0 para o peso e 0 para a idade. Imprima os dados da pessoa, na tela. Em seguida, altere os dados para "Texto", 99,99 e 10, para os mesmos dados respectivos. Imprima novamente. Por fim, peça que o usuário informe o nome, o peso e a idade da mesma pessoa, e imprima os dados na tela.
'''
pessoa = {
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso", pessoa["peso"])
print("Idade", pessoa["idade"])
print()

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso", pessoa["peso"])
print("Idade", pessoa["idade"])
print()

pessoa["nome"] = input("Digite seu nome: ")
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso", pessoa["peso"])
print("Idade", pessoa["idade"])
print()