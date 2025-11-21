'''
# Introdução a Programação Orientada a Objetos c/ Python
* Programação Orientada a Objetos
 - Classes e Objetos
  * Atributos e Métodos
 - Herança
  * Encapsulamento
  * Polimorfismo
 - Métodos "mágicos"
 - Abstração
'''

'''
# Classes
- Define-se um "modelo" para criação de objetos.
 * Objetos: instância com atributos e métodos
- Sintaxe de definição:
    class <classe>:
        <atributos> (Atributos são variáveis ou objetos)
        <métodos>   (Métodos são como funções convencionais)
'''

'''
# Relações entre Classes e Herança
- Classes podem formar relações entre si
 * Associação, agregação, composição, dependência, abstração
- Relação espacial: Herança
 * Classe(s) "pai" compartilha(m) atributos e/ou métodos com
   classe(s) filha(s)
   * Encapsulamento ; visibilidade
'''

'''
# Detalhes da POO em Python
- Referência para o próprio objeto: self
- Métodos "mágicos" (dunder methods)
 * __init__()
 * __str__()
 * __enter__()
 * __exit__()
 * __call__()
 
- Herança & Polimorfismo
    * class <classe_derivada>(super_classe (classe pai)>):

- Polimorfismo

- Encapsulamento
    * Público: <variável/função>
    * Protegido: _<variável/função>
    * Privado: __<variável/função>
    
- Onde definir atributos
 * No método __init__()
    * self.<variável> = <valor>
 * Atribuição/declaração logo no inicio da definição da classe
    * <variável> = <valor>
 * Dinâmicamente, dentro de métodos
    * self.<variável> = <valor>
'''
'''
Crie uma classe pai, chamado Animal, cujos atributos são o
nome e a espécie do animal, e o um único método é o fala().
Em seguida, crie duas subclasses derivadas de Animal:

    * Cachorro: com os atributos nome e raça. Inicialize a
    espécie do animal como "Cachorro". No método fala(),
    retorne um string dizendo algo como "<nome> é <raça> e
    late";
    * Gato: como atributos nome e cor. Inicialize a espécie
    do animal como "Gato". No método fala(), retorne uma string
    dizendo algo como "<nome> é <gato> e mia";
    * Crie dois objetos: um cão e um gato, ambos com os atributos
    que desejar
    * Imprima, na tela, todos os atributos de cada um dos objetos
    * Invoque a função fala() de cada um dos objetos e imprima
    o retorno na tela
'''
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def fala(self):
        return f"{self.nome} é um(a) {self.especie}"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca
        
    def fala(self):
        return f"{super().fala()} e late"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor
    
    def fala(self):
        return f"{super().fala()} e mia"
    
dog = Cachorro("Drago", "Caramelo")
cat = Gato("Garfield", "Rajado")

print("Atributos do Cachorro:")
print(f"Nome: {dog.nome}")
print(f"Raça: {dog.raca}")
print(f"Espécie: {dog.especie}")
print()
print(dog.fala())
print()
print()

print("Atributos do Gato:")
print(f"Nome: {cat.nome}")
print(f"Raça: {cat.cor}")
print(f"Espécie: {cat.especie}")
print()
print(cat.fala())
print()
