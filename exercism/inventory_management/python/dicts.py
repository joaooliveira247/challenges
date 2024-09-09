from collections import Counter

"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the
    `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return dict(Counter(items))


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Add or increment items in inventory using elements from the items
    `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    new_inventory: Counter = Counter(inventory)
    new_inventory.update(items)

    return dict(new_inventory)


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    new_inventory: Counter = Counter(inventory)
    new_inventory.subtract([x for x in items if x in new_inventory])

    return {k: v if v >= 0 else 0 for k, v in new_inventory.items()}


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory
    if item does not match.
    """

    new_inventory: Counter = Counter(inventory)
    try:
        new_inventory.pop(item)
    except KeyError:
        pass
    finally:
        return dict(new_inventory)


def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Create a list containing only available (item_name, item_count > 0)
    pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory
    dictionary.
    """

    inventory = {k: v for k, v in inventory.items() if v > 0}

    return list(inventory.items())
