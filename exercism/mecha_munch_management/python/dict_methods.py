"""Functions to manage a users shopping cart items."""

from typing import Iterable


def add_item(current_cart: dict[str, int], items_to_add: tuple[str]) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart: dict[str, int] = {}

    return add_item(cart, tuple(notes))


def update_recipes(
    ideas: dict[str, int], recipe_updates: list[tuple[str, dict[str, int]]]
) -> dict[str, int]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas
    section.
    :return: dict - updated "recipe ideas" dict.
    """

    for itens in recipe_updates:
        recipe: str = itens[0]
        ideas[recipe] = itens[1]

    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: dict[str, int], aisle_mapping: dict[str, list[str | int]]
) -> dict[str, list[str | int]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    return dict(
        sorted(
            {k: [v, *aisle_mapping[k]] for k, v in cart.items()}.items(),
            reverse=True,
        )
    )


def update_store_inventory(
    fulfillment_cart: dict[str, list[str | int]],
    store_inventory: dict[str, list[str | int]],
) -> dict[str, list[str | int]]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for k, v in fulfillment_cart.items():
        print(k, v)
        total: int = store_inventory[k][0] - v[0]
        store_inventory[k][0] = total if total > 0 else "Out of Stock"

    return store_inventory
