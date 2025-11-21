from dataclasses import dataclass
from typing import List

# ======================
# MODELOS DE DADOS
# ======================
@dataclass
class Cliente:
    id: int
    nome: str
    email: str
    celular: str

@dataclass
class Produto:
    id: int
    categoria: str
    nome: str
    preco: float
    estoque: int

# ======================
# BANCO DE DADOS EM MEMÓRIA
# ======================
class BancoDeDados:
    def __init__(self):
        self.clientes: List[Cliente] = []
        self.produtos: List[Produto] = []
        self.auto_id_cliente = 1
        self.auto_id_produto = 1

    # ----------------------
    # CLIENTES
    # ----------------------
    def cadastrar_cliente(self, nome: str, email: str, celular: str):
        cliente = Cliente(
            id=self.auto_id_cliente,
            nome=nome,
            email=email,
            celular=celular
        )
        self.clientes.append(cliente)
        self.auto_id_cliente += 1
        return cliente

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, id_cliente: int):
        return next((c for c in self.clientes if c.id == id_cliente), None)

    def remover_cliente(self, id_cliente: int):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False

    # ----------------------
    # PRODUTOS
    # ----------------------
    def cadastrar_produto(self, categoria: str, nome: str, preco: float, estoque: int):
        produto = Produto(
            id=self.auto_id_produto,
            categoria=categoria,
            nome=nome,
            preco=preco,
            estoque=estoque
        )
        self.produtos.append(produto)
        self.auto_id_produto += 1
        return produto

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id_produto: int):
        return next((p for p in self.produtos if p.id == id_produto), None)

    def remover_produto(self, id_produto: int):
        produto = self.buscar_produto(id_produto)
        if produto:
            self.produtos.remove(produto)
            return True
        return False

# ======================
# TESTE SIMPLES DO SISTEMA
# ======================
if __name__ == "__main__":
    db = BancoDeDados()

    # Cadastro de clientes
    db.cadastrar_cliente("Ana Silva", "ana@email.com", "1199999-0000")
    db.cadastrar_cliente("Carlos Souza", "carlos@email.com", "1188888-1111")

    # Cadastro de produtos
    db.cadastrar_produto("Informática", "Mouse Gamer", 150.00, 20)
    db.cadastrar_produto("Papelaria", "Caderno 100 folhas", 12.50, 50)

    # Listagens
    print("Clientes:")
    for c in db.listar_clientes():
        print(c)

    print("\nProdutos:")
    for p in db.listar_produtos():
        print(p)
