# Store API 🏪

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

- Create

    - Mapear uma exceção, caso dê algum erro de inserção e capturar na controller

        - Tasks

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/usecases/product.py#L20

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/controllers/product.py#L16

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/core/exceptions.py#L13

        - Tests

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/usecases/test_product.py#L17

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L24

- Update

    - Modifique o método de patch para retornar uma exceção de Not Found, quando o dado não for encontrado a exceção deve ser tratada na controller, pra ser retornada uma mensagem amigável pro usuário

        - Tasks

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/usecases/product.py#L42

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/controllers/product.py#L56

        - Tests

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/usecases/test_product.py#L58

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L89

    - ao alterar um dado, a data de updated_at deve corresponder ao time atual, permitir modificar updated_at também

        - Tasks

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/usecases/product.py#L43

        - Tests

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L98

- Filtros
    - cadastre produtos com preços diferentes
    - aplique um filtro de preço, assim: (price > 5000 and price < 8000)

        - Tasks

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/usecases/product.py#L48

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/controllers/product.py#L46

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/store_api/core/utils.py#L6

        - Tests

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/usecases/test_product.py#L58

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/usecases/test_product.py#L67

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L70

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L81

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L92

            - https://github.com/joaooliveira247/challenges/blob/main/dio/store_api/tests/controllers/test_product.py#L103


## This project was based 🤝:

https://github.com/digitalinnovationone/store_api
