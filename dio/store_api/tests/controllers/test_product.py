from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())

    content: dict = response.json()
    content = {
        k: v for k, v in content.items() if k not in ["id", "created_at", "updated_at"]
    }

    assert response.status_code == status.HTTP_201_CREATED
    assert content == product_data()


async def test_controller_get_should_return_sucess(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content: dict = {
        k: v
        for k, v in response.json().items()
        if k not in ["id", "created_at", "updated_at"]
    }

    assert response.status_code == status.HTTP_200_OK
    assert content == product_data()


async def test_controller_get_should_return_404(client, products_url, product_id):
    response = await client.get("{}{}".format(products_url, product_id))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "b065336f-a3d5-42a1-a45a-9a01566e97be not found."
    }


async def test_controller_get_all_should_return_sucess(
    client, products_url, products_inserted
):
    response = await client.get(f"{products_url}")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 1
