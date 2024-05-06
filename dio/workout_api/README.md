# Workout API 🏋️

![GitHub Pipenv locked Python version](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue)

## Requirements 🧑‍💻:
This project use a packaging and dependency management called [poetry](https://python-poetry.org/).
- Installation:

    `osx / linux / bashonwindows install instructions
    `

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```
    `
    windows powershell install instructions
    `
    ```bash
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
    ```
- Running:
    ```bash
    poetry install
    ```
    ```bash
    poetry shell
    ```

## Documentation 📜:

TODO
```bash
make run-docker
```

TODO args
```bash
make create-migrations --name
```

```bash
make run-migrations
```

```bash
make run
```

## Usage libraries :snake::
### [Typer v0.4.1](https://typer.tiangolo.com/).

## Challenges 🏆

- [adicionar query parameters nos endpoints]()
    - atleta
        - nome
        - cpf
- [customizar response de retorno de endpoints]()
    - get all
        - atleta
            - nome
            - centro_treinamento
            - categoria
- [Manipular exceção de integridade dos dados em cada módulo/tabela]()
    - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
    - status_code: 303
- [Adicionar paginação utilizando a lib: fastapi-pagination]()
    - limit e offset

## This project was based 🤝:

https://github.com/digitalinnovationone/workout_api