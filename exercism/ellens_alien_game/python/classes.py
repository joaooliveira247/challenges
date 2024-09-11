"""Solution to Ellen's Alien Game exercise."""

from __future__ import annotations


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    x_coordinate: int = 0
    y_coordinate: int = 0
    health: int = 3
    total_aliens_created: int = 0

    def __init__(self, x: int, y: int) -> None:
        self.x_coordinate = x
        self.y_coordinate = y
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, x: int, y: int) -> None:
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other_object) -> None:
        pass


def new_aliens_collection(
    alien_start_positions: list[tuple[int]],
) -> list[Alien]:
    return [Alien(*alien_coord) for alien_coord in alien_start_positions]
