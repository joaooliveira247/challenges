def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify that Pac-Man can eat a ghost if he is empowered by a power
      pellet.

    :param power_pellet_active: bool - does the player have an active power
    pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verify that Pac-Man has scored when a power pellet or
     dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    return any([touching_power_pellet, touching_dot])


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a
    ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active
    power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    # True False -> False
    # True True -> False
    # False True -> True

    if power_pellet_active:
        return False
    if not touching_ghost:
        return False
    return True


def win(
    has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool
) -> bool:
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active
    power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    # True False True -> False
    # False True True -> False
    # True False False -> True
    # True True True -> True

    if has_eaten_all_dots:
        return not lose(power_pellet_active, touching_ghost)
    return False
