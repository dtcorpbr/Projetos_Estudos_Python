'''
- Projetos complexos
********************

- Organização dos nomes e a hierarquia de invocações
depende da lógica do projeto: mais de 1 arquivo-fonte
- Convenções
 * Ponto de entrada: main.py
 __name__ == "__main__"
 * Módulos serão invocados diretamente ou indiretamente a partir do main.
 
 - Packages & Import
 *********************
 - É possível importar:
  * Uma única função de um arquivo-fonte(from)
  * Todo um arquivo-fonte e suas funções (import)
  * Um conjunto de arquivoas-fonte (package)
- Definindo packages
 * Cria-se o diretório como o nome do package: dentro do diretório, criam-se os módulos.
'''
'''
Defina dois arquivos-fonte: um main.py e um module1.py que contenha uma função arbitrária, definida por você. Dentro do main, importe o module1 e execute a função.
'''
# conteudo na pasta comando_import/Exercicio_1/
# conteudo na pasta comando_import/Exercicio_2/