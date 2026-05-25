import os
from datetime import datetime

from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from trello import TrelloClient

load_dotenv()

API_KEY = os.getenv("TRELLO_API_KEY")
API_TOKEN = os.getenv("TRELLO_TOKEN")
API_SECRET = os.getenv("TRELLO_SECRET")


def get_temporal_context() -> str:
    now = datetime.now()
    return now.strftime("%Y/%m/%d %H:%M:%S")


def add_task(task_name: str, task_description: str, due_date: str):
    client = TrelloClient(
        api_key=API_KEY, api_secret=API_SECRET, token=API_TOKEN
    )

    boards = client.list_boards()

    my_board = [b for b in boards if b.name == "Workflow"][0]

    lists = my_board.list_lists()

    my_list = [l for l in lists if l.name.upper() == "TO DO"][0]

    my_list.add_card(task_name, task_description, due=due_date)


def list_tasks(status: str = "all"):
    client = TrelloClient(
        api_key=API_KEY, api_secret=API_SECRET, token=API_TOKEN
    )

    boards = client.list_boards()

    my_board = [b for b in boards if b.name == "Workflow"][0]

    lists = my_board.list_lists()

    match status.lower:
        case "all":
            filtred_lists = lists
        case "to do":
            filtred_lists = [
                l for l in lists if l.name.upper() in ["TO DO", "TODO"]
            ]
        case "doing":
            filtred_lists = [l for l in lists if l.name.upper() == "DOING"]
        case "done":
            filtred_lists = [l for l in lists if l.name.upper() == "DONE"]
        case _:
            filtred_lists = lists

    tasks = []

    for f_list in filtred_lists:
        cards = f_list.list_cards()
        for card in cards:
            tasks.append(
                {
                    "name": card.name,
                    "description": card.description,
                    "expired_at": card.due,
                    "status": f_list.name,
                    "id": card.id,
                }
            )


def change_status_task(nome_da_task: str, novo_status: str) -> str:
    try:
        client = TrelloClient(
            api_key=API_KEY, api_secret=API_SECRET, token=API_TOKEN
        )

        boards = client.list_boards()
        meu_board = [b for b in boards if b.name == "Workflow"][0]
        listas = meu_board.list_lists()

        status_map = {"to do": "TO DO", "doing": "DOING", "done": "DONE"}

        nome_lista_destino = status_map.get(novo_status.lower())

        if not nome_lista_destino:
            return f"❌ Inavalid Status. Use: 'to do', 'doing' or 'done'"

        lista_destino = next(
            (
                l
                for l in listas
                if l.name.upper() == nome_lista_destino.upper()
            ),
            None,
        )

        if not lista_destino:
            return f"❌ List '{nome_lista_destino}' not found in the board"

        card_encontrado = None
        lista_origem = None

        for lista in listas:
            cards = lista.list_cards()
            card_encontrado = next(
                (c for c in cards if c.name.lower() == nome_da_task.lower()),
                None,
            )
            if card_encontrado:
                lista_origem = lista
                break

        if not card_encontrado:
            return f"❌ Card '{nome_da_task}' not found"

        card_encontrado.change_list(lista_destino.id)
        return (
            f"✅ '{nome_da_task}': {lista_origem.name} → {lista_destino.name}"
        )
    except Exception as e:
        return f"❌ Erro: {str(e)}"


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Task manager agent",
    instruction="""
    You are a task manager agent
    Your function is recieve one task and create a card in trello with title and description
    You must ask for day task and separete each in cards
    You start the chat asking how are the day tasks with date using the tool get_temporal_context
    Your functions are:
        1. add new task
        2. list tasks or filter by status
        3. mark all complete tasks
        4. remove tasks (if it required)
        5. change task status (it can be in english)
        7. generate temporal context.
    """,
    tools=[add_task, get_temporal_context, list_tasks, change_status_task],
)
