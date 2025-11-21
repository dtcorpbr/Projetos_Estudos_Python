'''
Modele um dicionário que seja capaz de armazenar os dados de um produto, a saber: Um número de identificação (id), o nome do produto e o seu preço.
 * Faça com que o usuário seja capaz de adicionar produtos (no máximo 5). A cada nova inserção, devese imprimir, na tela, a quantidade de produtos já cadastrados, bem como o id, nome e preço de cada produto.
'''
produtos = []

for _ in range(5):
    produto = {}
    produto['id'] = int(input('Digite o ID do produto: '))
    produto['nome'] = input('Digite o nome do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    
    produtos.append(produto)
    print(f'\nProdutos cadastrados: {len(produtos)}')
    
    for p in produtos:
        print(f"ID: {p['id']}, Nome: {p['nome']}, Preço: R${p['preco']:.2f}")
    print()
