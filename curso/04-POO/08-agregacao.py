
# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []
        self._servicos = []

    def total(self):
        s_soma = sum([s.preco for s in self._servicos])
        p_soma = sum([p.preco for p in self._produtos])
        return s_soma + p_soma

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
            
    def inserir_servicos(self, *servicos):
        for servico in servicos:
            self._servicos.append(servico)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
    
    def listar_servicos(self):
        print()
        for servico in self._servicos:
            print(servico.nome, servico.preco)
        print()
        
    def limpar_carrinho(self):
        self._produtos = []
        self._servicos = []


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Servico:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
                

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
s1 = Servico('instalação', 30, 'Instalação de ar')
carrinho.inserir_servicos(s1)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
carrinho.listar_servicos()
print(carrinho.total())
carrinho.limpar_carrinho()
print(carrinho.total())