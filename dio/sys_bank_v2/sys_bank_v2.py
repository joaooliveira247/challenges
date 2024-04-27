from __future__ import annotations
from dataclasses import dataclass, field
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
    conta: ContaCorrente


@dataclass
class Bank:
    clients: list[Cliente] = field(default_factory=list)


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
        numero_conta=len(bank.clients) + 1,
        saldo=saldo,
        saques=saques,
        limite=limite,
    )


def get_conta(banco: Bank, numero: int) -> ContaCorrente | None:
    for conta in banco.clients:
        if conta.conta.numero_conta == numero:
            return conta.conta
    print("Conta não encontrada")
    return None


def criar_usuario(
    bank: Bank,
    conta: ContaCorrente,
    *,
    nome: str,
    data_nascimento: str,
    cpf: str,
    endereco: str,
) -> Cliente | None:
    for cliente in bank.clients:
        if cpf in cliente.cpf:
            print("CPF já cadastrado.")

    cliente = Cliente(
        nome,
        data_nascimento,
        cpf,
        endereco,
        conta=conta,
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
    conta.extrato += "R$ {:.2f} removido.\n".format(valor)
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
            case EnumOption.criar_usuarios:
                user = {
                    "nome": "",
                    "data_nascimento": "",
                    "cpf": "",
                    "endereco": "",
                }
                for v in user.keys():
                    user_input = input(f"Digite o seu {v}".replace("_", " "))
                    user[v] = user_input
                saldo_inicial = input("Digite o saldo inicial.")
                criar_usuario(
                    bank,
                    criar_conta(
                        bank,
                        saldo=float(saldo_inicial),
                    ),
                    **user,
                )
            case EnumOption.sacar:
                conta_id, valor = input("Digite o número da sua conta e valor.").split(
                    " ",
                )
                conta = get_conta(bank, int(conta_id))
                if conta:
                    sacar(conta, float(valor))
                continue
            case EnumOption.depositar:
                conta_id, valor = input("Digite o número da sua conta e valor.").split(
                    " ",
                )
                conta = get_conta(bank, int(conta_id))
                if conta:
                    depositar(conta, float(valor))
                continue
            case EnumOption.extrato:
                conta_id = input("Digite o número da conta:\n")
                conta = get_conta(bank, int(conta_id))
                ver_extrato(conta)
                continue
            case EnumOption.listar_usuarios:
                print(bank.clients)

            case EnumOption.exit_:
                break
            case None:
                print("Opção invalida")


if __name__ == "__main__":
    main()
