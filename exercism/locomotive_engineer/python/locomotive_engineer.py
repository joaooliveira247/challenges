"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args: tuple[int]) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    end, new = each_wagons_id[:2], each_wagons_id[2:]
    return [new[0], *missing_wagons, *new[1:], *end]


def add_missing_stops(
    route: dict[str, str], **kwargs: dict[str, str]
) -> dict[str, str]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(kwargs.values())
    return route


def extend_route_information(
    route: dict[str, str], more_route_information: dict[str, str]
) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    w = []

    for i in range(len(wagons_rows)):
        z = []
        for j in range(len(wagons_rows)):
            z.append(wagons_rows[j][i])
        w.append(z)

    return w
