from dataclasses import dataclass


@dataclass
class Venda:
    produto: str
    quantidade: int
    valor: float


class Categoria:
    def __init__(self, nome: str):
        self.nome = nome
        self.vendas: list[Venda] = []

    def adicionar_venda(self, venda: Venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
            return

    def total_vendas(self) -> float:
        total: float = sum([(x.valor) for x in self.vendas])

        return total


def main():
    categorias: list[Categoria] = []

    for _ in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for _ in range(2):
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(",")
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)

    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        # TODOS: Exibir o total de vendas usando o método total_vendas:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas()}")


if __name__ == "__main__":
    main()
