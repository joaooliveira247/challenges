# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
from datetime import datetime


class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ano_atual = datetime.now().year

    def verificar_antiguidade(
        self,
    ) -> str:
        if (self.ano_atual - self.ano) > 20:
            return "Veículo antigo"
        return "Veículo novo"

    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:


# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
