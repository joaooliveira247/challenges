from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class EnumOption(str, Enum):
    sacar = "s"
    depositar = "d"
    extrato = "e"
    listar_usuarios = "ls"
    criar_usuarios = "c"
    exit_ = "q"


@dataclass
class ContaCorrente:
    numero_conta: int
    agencia: str = "0001"
    saldo: int = 0
    saques: int = 3
    limite: float = 500.00
    extrato: str = ""


@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    cpf: str
    endereco: str
    contas: list[ContaCorrente] | None = None


@dataclass
class Bank:
    clients: list[Cliente] = []


def menu() -> EnumOption | None:
    MENU: str = """
[d] Depositar
[s] Sacar
[e] Extrato
[ls] Listar usuarios
[c] Criar usuarios
[q] Sair
"""
    try:
        return EnumOption(input(MENU))
    except ValueError:
        return None


def criar_conta(
    bank: Bank,
    saldo: float,
    saques: int = 3,
    limite: float = 500.00,
) -> ContaCorrente:
    return ContaCorrente(
        len(bank.clients) + 1,
        saldo,
        saques,
        limite,
    )


def criar_usuario(
    bank: Bank,
    conta: ContaCorrente,
    nome: str,
    data_nascimento: str,
    cpf: str,
    endereco: str,
    /,
) -> Cliente | None:
    for cliente in bank.clients:
        if cpf in cliente.cpf:
            print("CPF já cadastrado.")

    cliente = Cliente(
        nome,
        data_nascimento,
        cpf,
        endereco,
        contas=[conta],
    )

    bank.clients.append(cliente)
    print(f"cliente {cliente.nome} criado.")
    return cliente


def depositar(conta: ContaCorrente, valor: float) -> None:
    conta.saldo += valor
    conta.extrato += "R$: {:.2f} depositado.\n".format(valor)
    return


def sacar(conta: ContaCorrente, valor: float) -> None:
    if conta.saldo < valor:
        print("Saldo insuficiente.")
        return
    conta.saldo -= valor
    conta.saques -= 1
    return


def ver_extrato(conta: ContaCorrente) -> None:
    print(conta.extrato)
    print(f"Saldo: {conta.saldo}")
    return


def main() -> None:
    bank = Bank()
    while True:
        user_input = menu()
        match user_input:
            case EnumOption.sacar:
                conta, valor = input("Digite o número da sua conta e valor.").split(
                    " ",
                )
                sacar(bank[conta], float(valor))
                continue
            case EnumOption.depositar:
                conta, valor = input("Digite o número da sua conta e valor.").split(
                    " ",
                )
                depositar(bank[conta], float(valor))
                continue
            case EnumOption.extrato:
                ...
            case None:
                print("Opção invalida")


if __name__ == "__main__":
    main()
