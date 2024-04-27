import re


def validate_numero_telefone(phone_number: str) -> str:
    pattern = r"\(\d{2}\) \d{5}-\d{4}"

    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    return "Número de telefone inválido."


def main() -> None:
    phone_number = input()

    result: str = validate_numero_telefone(phone_number)
    print(result)


if __name__ == "__main__":
    main()
