def recomendar_plano(consumo: float) -> str:
    # To solve this type of proble i prefer use match statment,
    # but some web interprets run in python 3.8
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    if consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    if consumo > 20:
        return "Plano Premium Fibra - 300Mbps"


def main() -> None:
    consumo = float(input())
    print(recomendar_plano(consumo))


if __name__ == "__main__":
    main()
