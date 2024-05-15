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
