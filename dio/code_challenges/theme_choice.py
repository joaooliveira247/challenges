# Dicionário para agrupar participantes por tema
eventos: dict[str, list[str]] = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    user_input = input().strip().split(",")
    if eventos.get(user_input[1]):
        eventos[user_input[1]].append(user_input[0])
    else:
        eventos[user_input[1]] = [user_input[0]]


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
