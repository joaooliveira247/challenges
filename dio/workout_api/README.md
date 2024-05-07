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

- 🐋 Start docker with database.

```bash
make run-docker
```

- 📋 Create a migration and put it on staging area.

```bash
make create-migrations name
```

- 📋 Run migrate on models and databases.

```bash
make run-migrations
```

- 🏋️ Run API

```bash
make run
```

## Usage libraries 🐍:

### [Fastapi](https://fastapi.tiangolo.com/)

### [uvicorn](https://www.uvicorn.org/)

### [sqlalchemy](https://www.sqlalchemy.org/)

### [Typer](https://typer.tiangolo.com/)

### [Alembic](https://alembic.sqlalchemy.org/en/latest/)

### [Pydantic & Pydantic-settings](https://docs.pydantic.dev/latest/)

### [asyncpg](https://pypi.org/project/asyncpg/)

### [Fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/)

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