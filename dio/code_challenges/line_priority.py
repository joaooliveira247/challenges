# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))


def line_order(line: list[tuple[str, int, str]]) -> list[str]:
    urgentes = []
    idosos = []
    demais = []

    for nome, idade, status in line:
        if status == "urgente":
            urgentes.append((nome, idade))
        elif idade >= 60:
            idosos.append(nome)
        else:
            demais.append(nome)

    # Ordena urgentes por idade (decrescente)
    urgentes.sort(key=lambda x: x[1], reverse=True)
    urgentes_nomes = [nome for nome, _ in urgentes]

    return urgentes_nomes + idosos + demais


# TODO: Exiba a ordem de atendimento com título e vírgulas:
def output(line: list[str]) -> None:
    print(f"Ordem de Atendimento: {', '.join(line)}")


if __name__ == "__main__":
    ordered_line = line_order(pacientes)
    output(ordered_line)
