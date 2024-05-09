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

- [adicionar query parameters nos endpoints](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/athlete.py#L129)
    - atleta
        - nome
        - cpf / ssn
- [customizar response de retorno de endpoints](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/athlete.py#L100)
    - get all
        - atleta
            - nome
            - centro_treinamento
            - categoria
- Manipular exceção de integridade dos dados em cada módulo/tabela.

    - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”

    - status_code: 303

        - [atleta](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/athlete.py#L83)

        - [centro de treinamento](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/training_center.py#L34)

        - [categoria](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/category.py#L31)

- Adicionar paginação utilizando a lib: fastapi-pagination.
    - limit e offset

        - [atletas](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/athlete.py#L104)

        - [categoria](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/category.py#L48)

        - [centro treinamento](https://github.com/joaooliveira247/challenges/blob/main/dio/workout_api/workout_api/controllers/training_center.py#L51)

## This project was based 🤝:

https://github.com/digitalinnovationone/workout_api