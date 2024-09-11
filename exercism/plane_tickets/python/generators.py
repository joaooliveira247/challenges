"""Functions to automate Conda airlines ticketing system."""

from typing import Generator


def generate_seat_letters(number: int) -> Generator[str, None, None]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters: tuple[str] = "A", "B", "C", "D"
    # 0, 1, 2, 3 -> 5 - A, B, C, D
    for idx in range(1, number + 1):
        yield letters[(idx + 3) % 4]


def generate_seats(number: int) -> Generator[str, None, None]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_numbers_counter: int = 1
    seats_numbers: list[int] = []

    for _ in range(number):
        if seat_numbers_counter == 13:
            seat_numbers_counter += 1
        seats_numbers.append(seat_numbers_counter)
        if len(seats_numbers) % 4 == 0:
            seat_numbers_counter += 1

    seats: list[tuple[str, int]] = list(
        zip(generate_seat_letters(number), seats_numbers)
    )

    print(seats)

    for seat, number in seats:
        yield f"{number}{seat}"


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of
    passengers.
    :return: dict - with the names of the passengers as keys and seat
    numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats: list[str] = zip(passengers, list(generate_seats(len(passengers))))

    return {passenger: seat for passenger, seat in seats}


def generate_codes(
    seat_numbers: list[str], flight_id: str
) -> Generator[str, None, None]:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket: str = f"{seat}{flight_id}"
        yield ticket.ljust(12, "0")
