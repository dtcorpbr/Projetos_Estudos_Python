'''
# Arquivo
- São vistos pelo SO como um recurso
 * Armazenamento de grandes quantidades de informação.
- Manipulados "fora do ambiente do programa"
 * Persistidos em memória secundária (HD, SSD, etc).
 * Leitura /escrita em memória primária (RAM).
- Arquivos: Características
 * Tamanho
 * Extensão (.json, .csv, etc)
 * Endereço em memória (caminho)
 * Permissões (leitura, escrita, execução)
 * Informações sobre tempo (criação, modificação, acesso)
 * Proprietário (usuário, grupo)
 * Cuidado: vazamento de recursos (memória)
'''
'''
# Operações
 - Abrir
 <arquivo> = open(<caminho>, <modo>)
 
  * Modo leitura: 'r' - padrão
  * Modo escrita: 'w' - apaga o conteúdo anterior
  * Modo append: 'a' - mantém o conteúdo anterior
  * modo leitura e escrita (append): 'a+'
- Precaussão: abrir & fechar antes de o programa encerrar
- Fechar: <arquivo>.close()
 * Problema: programa encerra abruptamente....
 * Boa prática:
    with open(<caminho>, <modo>) as <arquivo>:
        <operações com o arquivo>
 * Arquivo é fechado, mesmo em caso de falha
- Leitura
 * <arquivo>.read()
 * <arquivo>.readline(<iterável>)
 
- Escrita
 * <arquivo>.write(<conteúdo>)
 * <arquivo>.writelines(<conteúdo iterável>)
 
- Navegando pelo arquivo
 * for <linha> in <arquivo>:
- Posicionamento do cursor
 * <arquivo>.seek(<bytes>)
- Cuidado: posicionamento do cursor
 * Estamos fazendo leitura, ou escrita? Em qual parte?
'''
'''
- Crie um programa que peça e continue pedindo para que
o usuário informe palavras e vá armazenando tais palavras em um arquivo. Quando o usuário digitar "/exit", você deve interromper as leituras (a palavra "/exit" não deve ser armazenada no arquivo). Por fim, imprima na tela, o conteúdo do arquivo.
'''

nome_arquivo = input("Digite o nome do arquivo para armazenar as palavras: ")

with open(nome_arquivo, 'w') as arquivo:
    while True:
        palavra = input("Digite uma palavra (ou /exit para encerrar): ")
        if palavra == "/exit":
            break
        arquivo.write(f"{palavra}\n")
print("Palavras armazenadas com sucesso. . . \n")

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteudo do arquivo: ")
    print(conteudo)