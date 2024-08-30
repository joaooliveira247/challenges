def identificar_termo_bi(termo: str) -> str:
    terms: dict[str, str] = {
        "ETL": (
            "Processo de extrair, transformar e carregar dados de diversas" " fontes."
        ),
        "Data Warehousing": (
            "Armazenamento centralizado de dados para análise e relatórios."
        ),
        "Dashboard": ("Ferramenta visual para monitoramento e análise de métricas."),
        "Data Mining": (
            "Descoberta de padrões e insights em grandes conjuntos de dados."
        ),
    }
    result: str | None = terms.get(termo)
    return "Termo não reconhecido" if result is None else result


def main() -> None:
    entrada = input()

    print(identificar_termo_bi(entrada))


if __name__ == "__main__":
    main()
