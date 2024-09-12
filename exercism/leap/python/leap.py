def leap_year(year: int) -> bool:
    if year % 100 == 0 and year % 400 == 0:
        return True
    last_two: str = str(year)[2:]
    return True if int(last_two) % 4 == 0 and last_two != "00" else False
