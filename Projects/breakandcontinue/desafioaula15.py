'''
Crie um programa que mostre, na tela, um contador. O contador deve der inicializado com. O usuário deve ter a opção de incrementar uma unidade ao contador, ou de encerrar o programa. Enquanto o usuário continuar decidindo incrementar o contador, o programara não deve encerrar. Oprograma encerra somente quando o usuário decidir. Utilize um laço com os comandos break e continue.
'''
contador = 0
while True:
    print(f'Contador: {contador}')
    opcao = input('Deseja incrementar o contador? (s/n): ').strip().lower()
    if opcao == 's':
        contador += 1
        continue
    elif opcao == 'n':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida. Por favor, responda com "s" ou "n".')