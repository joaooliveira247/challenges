def identificar_conceito_etl(conceito: str) -> str:
    terms: dict[str, str] = {
        "Extract": "Processo de coletar dados de diversas fontes.",
        "Transform": "Processo de converter dados para um formato adequado.",
        "Load": (
            "Carregamento de dados transformados em banco de dados ou" " warehouse."
        ),
        "Data Integration": ("Unificação de dados provenientes de múltiplas fontes."),
    }
    result: str | None = terms.get(conceito)
    return "Conceito não reconhecido" if result is None else result


def main() -> None:
    entrada = input()

    print(identificar_conceito_etl(entrada))


if __name__ == "__main__":
    main()
