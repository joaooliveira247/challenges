def to_binary(hex: str) -> str:
    binary = int(hex, 16)
    return bin(binary)[2:]


def main() -> None:
    print(to_binary("0xFF"))
    print(to_binary("0xAA"))
    print(to_binary("0xFA"))


if __name__ == "__main__":
    main()
