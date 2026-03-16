from socket import gethostbyaddr


def get_domain(ip_address: str) -> str:
    return gethostbyaddr(ip_address)[0]


def main() -> None:
    dns_tests: list[str] = ["8.8.8.8", "8.8.4.4", "1.1.1.2", "1.1.1.3"]

    [print(get_domain(dns)) for dns in dns_tests]


if __name__ == "__main__":
    main()
