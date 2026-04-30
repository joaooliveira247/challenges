# 💰 Bank API

## 💻 Requirements:

### [`Docker`](https://www.docker.com/) & [`Docker compose`](https://docs.docker.com/compose/)

### [`UV`](https://docs.astral.sh/uv/)

## Installation & Running:

### Docker

```bash
docker compose up -d
```

### uv

This project uses a package and dependency maganer called uv. [Installation guide](https://docs.astral.sh/uv/getting-started/installation/)

1º step: `uv installation`

```curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2º step: `Creating virtual enviroment and activating`

```bash
uv venv
```

```bash
source .venv/bin/activate
```

> **__Note:__**
>
> On Linux and macOS, the commands to install and activate the virtual environment are the same. For Windows, please refer to the official documentation.

3º step: `install all dependencies`

```bash
uv sync --all-groups
```

> **__Warning:__**
>
> Please remember to configure the `.env` file. [.env example file](./.env.example)

## 📜 Documentation:

don't forget to setup `.env` file an example is available in `.env.example`


## 🐍 Usage libraries:

- [asyncpg >=0.30.0](https://pypi.org/project/asyncpg/)
- [fastapi >=0.115.8](https://pypi.org/project/fastapi/)
- [pydantic >=2.10.6](https://pypi.org/project/pydantic/)
- [pydantic-settings >=2.7.1](https://pypi.org/project/pydantic-settings/)
- [python-jose >=3.5.0](https://pypi.org/project/python-jose/)
