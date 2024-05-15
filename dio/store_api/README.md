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

### [Pydantic & Pydantic-settings](https://docs.pydantic.dev/latest/)

### [Motor]()


## Challenges 🏆


## This project was based 🤝:

https://github.com/digitalinnovationone/store_api
