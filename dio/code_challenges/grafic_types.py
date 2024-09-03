def filtrar_visuais(lista_visuais: str) -> str:
    visuais: list[str] = [visual.lower() for visual in lista_visuais.split(", ")]
    return ", ".join(sorted([visual.title() for visual in set(visuais)]))


def main() -> None:
    entrada_usuario = input()

    saida = filtrar_visuais(entrada_usuario)
    print(saida)


if __name__ == "__main__":
    main()
