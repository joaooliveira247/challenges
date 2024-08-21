from dataclasses import dataclass


@dataclass
class Venda:
    produto: str
    quantidade: int
    valor: float


class Relatorio:
    def __init__(self):
        self.vendas: list[Venda] = []

    def adicionar_venda(self, venda: Venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
            return

    def calcular_total_vendas(self) -> float:
        total: float = sum([(x.valor * x.quantidade) for x in self.vendas])

        return total


def main():
    relatorio = Relatorio()

    for _ in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)

    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    print(f"Total de Vendas: {relatorio.calcular_total_vendas()}")


if __name__ == "__main__":
    main()
