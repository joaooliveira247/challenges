# Docker Dio Challenge

Essa Arquitetura eu uso em um projeto pessoal (backend em Go, database postgres)

Optei por não deixar o backend todo no escopo do projeto, pois fugiria do contexto por seu um projeto relativamente grande.

## Compose

```yaml
version: '3.1'

services:

  book_store:
    image: postgres:11-alpine
    restart: "no"
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: passwd
      POSTGRES_DB: book_store
    networks:
      - book_store_backend
    ports:
      - 5432:5432

  book_api_1:
    build:
      context: .
      dockerfile: Dockerfile
    networks:
      - book_store_backend
    volumes:
      - ./:/app
    expose:
      - 8000

  book_api_2:
    build:
      context: .
      dockerfile: Dockerfile
    networks:
      - book_store_backend
    volumes:
      - ./:/app
    expose:
      - 8000

  book_api_3:
    build:
      context: .
      dockerfile: Dockerfile
    networks:
      - book_store_backend
    volumes:
      - ./:/app
    expose:
      - 8000

  nginx:
    image: nginx:alpine
    depends_on:
      - book_api_1
      - book_api_2
      - book_api_3
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    ports:
      - 80:80
    networks:
      - book_store_backend

networks:
  book_store_backend:

```

## Dockerfile

```Dockerfile
FROM golang:1.23-alpine

WORKDIR /app

RUN go install github.com/air-verse/air@latest

COPY go.mod go.sum ./
RUN go mod download

CMD ["air", "run"]
```

## Nginx Config

```nginx
events {}

http {
    upstream backend {
        server book_api_1:8000;
        server book_api_2:8000;
        server book_api_3:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

# Alternativas em Cloud

Usando a AWS que é um serviço que eu tenho familiaridade.

### Arquitetura não gerenciada

Caso queira uma aplicação não gerenciada você pode optar por uma maquina `EC2`.

### Arquitetura gerenciada

- AWS `RDS` para o banco de dados.

- AWS `ECS` para a aplicação em container.

- AWS `ELB` para substituir o nginx

- AWS `Lambda` pode ser uma solução para rodar o backend também

