from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())

    content: dict = response.json()
    content = {
        k: v
        for k, v in content.items()
        if k
        not in [
            "id",
            "created_at",
            "updated_at",
        ]
    }

    assert response.status_code == status.HTTP_201_CREATED
    assert content == product_data()


async def test_controller_create_product_already_exists(
    client, products_url, product_inserted
):
    data = product_data()
    response = await client.post(products_url, json=data)
    assert response.status_code == status.HTTP_406_NOT_ACCEPTABLE
    assert response.json() == {
        "detail": f"Product already exists in id:{product_inserted.id}"
    }


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


async def test_controller_patch_should_return_sucess(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"quantity": 40}
    )

    product = product_data()
    product["quantity"] = 40
    product_in = {
        k: v
        for k, v in response.json().items()
        if k not in ["id", "created_at", "updated_at"]
    }

    assert response.status_code == status.HTTP_202_ACCEPTED
    assert product_in == product


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_raise_404(client, products_url, product_id):
    response = await client.delete(f"{products_url}{product_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND

    assert response.json() == {
        "detail": "b065336f-a3d5-42a1-a45a-9a01566e97be not found."
    }
