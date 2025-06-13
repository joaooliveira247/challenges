# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))


# TODO: Ordene por prioridade: urgente > idosos > demais:
def line_order(line: list[tuple[str | int]]) -> list[str]:
    priority_line = []
    normal_line = []
    for people in line:
        if people[2] == "urgente":
            if people[1] >= 60:
                priority_line.insert(0, people[0])
                continue
            priority_line.append(people[0])
            continue
        if people[1] >= 60:
            normal_line.insert(0, people[0])
            continue
        normal_line.append(people[0])

    priority_line.extend(normal_line)

    return priority_line


# TODO: Exiba a ordem de atendimento com título e vírgulas:
def output(line: list[str]) -> None:
    print(f"Ordem de Atendimento: {', '.join(line)}")


if __name__ == "__main__":
    ordered_line = line_order(pacientes)
    output(ordered_line)
