'''
Crie um programa que cadastra os dados de clientes (nome, cpf,
telefone, e-mail e endereço) em um arquivo. O usuário deve poder
cadastrar tantos clientes quanto desejar. Utilize JSON.
Você deve ser capaz de:
 * Buscar um cliente específico através de seu CPF;
 * Alterar os dados de um cliente;
 * Apagar um cliente;
 * Mostrar todos os clientes na tela.
'''
import json
import os

Arquivo = "clientes.json"

# -------------------------------------------------
# clientes.json | > Carregar arquivo
# -------------------------------------------------
def carregar_clientes():
    if not os.path.exists(Arquivo):
        return[]
    with open(Arquivo, 'r', encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
# -------------------------------------------------
# clientes.json | > Salvar arquivo
# -------------------------------------------------
def salvar_clientes(clientes):
    with open(Arquivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
        
# -------------------------------------------------
# clientes.json | > Cadastrar novo cliente
# -------------------------------------------------
def cadastrar_cliente():
    clientes = carregar_clientes()
    
    cpf = input("CPF: ")
    
    # Validação (Verificar se já existe)
    for c in clientes:
        if c["cpf"] == cpf:
            print("⚠ Já existe um cliente cadastrado com esse CPF!")
            return
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    clientes.append(cliente)
    salvar_clientes(clientes)
    print("✔ Cliente cadastrado com sucesso!")

# -------------------------------------------------
# clientes.json | > Buscar cliente por CPF
# -------------------------------------------------
def buscar_cliente():
    cpf = input("Digite o COF para busca: ")
    clientes = carregar_clientes()
    
    for c in clientes:
        if c["cpf"] == cpf:
            print("\nCliente encontrado: ")
            print(json.dump(c, indent=4, ensure_ascii=False))
            return
    
    print("❌ Cliente não encontrado.")

# -------------------------------------------------
# clientes.json | > Listar clientes
# -------------------------------------------------
def mostrar_todos():
    clientes = carregar_clientes()
    
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- LISTA DE CLIENTES ---")
    for c in clientes:
        print(json.dumps(c, indent=4, ensure_ascii=False))
        print("---------------------------")
        
# -------------------------------------------------
# clientes.json | > Alterar dados de cliente
# -------------------------------------------------
def alterar_cliente():
    cpf = input("Digite o CPF do cliente para alterar: ")
    clientes = carregar_clientes()
    
    for c in clientes:
        if c["cpf"] == cpf:
            print("Cliente encontrado! Deixe em branco para não alterar.")
            
            nome = input(f"Nome [{c['nome']}]: ") or c["nome"]
            telefone = input(f"Telefone [{c['telefone']}]: ") or c["telefone"]
            email = input(f"E-mail [{c['email']}]: ") or c["email"]
            endereco = input(f"Endereco[{c['endereco']}]: ") or c["endereco"]
            
            c["nome"] = nome
            c["telefone"] = telefone
            c["email"] = email
            c["endereco"] = endereco
            
            salvar_clientes(clientes)
            print("✔ Dados atualizados com sucesso!")
            return
        
    print("❌ Cliente não encontrado.")

# -------------------------------------------------
# clientes.json | > Apagar cliente
# -------------------------------------------------
def apagar_cliente():
    cpf = input("Digite o CPF do cliente para apagar: ")
    clientes = carregar_clientes()
    
    for c in clientes:
        if c["cpf"] == cpf:
            clientes.remove(c)
            salvar_clientes(clientes)
            print("✔ Cliente removido com sucesso!")
            return

    print("❌ Cliente não encontrado.")

# -----------------------------------------------------------
# MENU PRINCIPAL
# -----------------------------------------------------------

def menu():
    while True:
        print("\n=== SISTEMA DE CADASTRO DE CLIENTES ===")
        print("1 - Cadastrar cliente")
        print("2 - Buscar cliente por CPF")
        print("3 - Alterar cliente")
        print("4 - Apagar cliente")
        print("5 - Mostrar todos os clientes")
        print("0 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_cliente()
        elif opc == "2":
            buscar_cliente()
        elif opc == "3":
            alterar_cliente()
        elif opc == "4":
            apagar_cliente()
        elif opc == "5":
            mostrar_todos()
        elif opc == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")