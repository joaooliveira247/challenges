class BaseException(Exception):
    message: str = "Internal Server Error"

    def __init__(self, message: str | None = None) -> None:
        if message:
            self.message = message


class DBNotFoundValueException(BaseException):
    message = "Not Found"


class ProductAlreadyExists(BaseException):
    ...


class FilterFailureException(BaseException):
    ...
