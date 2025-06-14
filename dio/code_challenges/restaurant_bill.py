class Pedido:
    def __init__(self):
        self.itens = []

    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self, preco: float):
        self.itens.append(preco)

    def total(self) -> str:
        return f"{sum(self.itens):.2f}"

        # TODO: Adicione o preço do item à lista:

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:

    # TODO: Retorne a soma de todos os preços


quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    # TODO: Chame o método adicionar_item corretamente:
    pedido.adicionar_item(float(preco))

# TODO: Exiba o total formatado com duas casas decimais:
print(pedido.total())
