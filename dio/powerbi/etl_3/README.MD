# Desafio ETL DIO

## Cloud x Container

optei por usar um container com postgres pois na azure implicava em cobranças.

[docker-compose.yaml](./docker-compose.yaml)

## Steps

### Step 1

- Converti os scripts de MySQL -> Postgres

### Step 2


- Após subir o container com o comando `docker compose up -d`.

- Usei o DBeaver para executar as Queries de Criaçãodas das tabelas e inserção dos dados.

### Step 3

- Carreguei os dados no PowerBI.

#### Transformando os dados Usando o PowerQuery

- public_departament

    - Trocado o tipo de dados

        |Nome|Antigo|Novo|
        |:---:|:---:|:---:|
        |mgr_ssn|Texto|Inteiro|

- public_dependant

    - Trocado o tipo de dados

        |Nome|Antigo|Novo|
        |:---:|:---:|:---:|
        |ssn|Texto|Inteiro|

- public_employee

    - Trocado o tipo de dados

        |Nome|Antigo|Novo|
        |:---:|:---:|:---:|
        |ssn|texto|Inteiro|
        |super_ssn|texto|Inteiro|

    - Separada cidade e estado no endereço

    - Excluido coluna de estados, pois todos registros são do texas

    -renomeado campo resultante de cidade

    - adicionado sufixo `.` em minit

    - Mesclado colunas (fname, minit, lname)

    - Mudado nome de coluna resultande de mesclagem para name

    - Deletada colunas (fname, minit, lname)

- public_works_on

    - Trocado o tipo de dados

        |Nome|Antigo|Novo|
        |:---:|:---:|:---:|
        |essn|Texto|Inteiro|
        |hours|Número Decimal|Duração|

- Join public works_on com employee
