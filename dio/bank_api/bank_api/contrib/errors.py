class BaseError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class UnexpectedError(BaseError):
    def __init__(self, message: str, location: str, resource: str) -> None:
        super().__init__(f"[{location}] ({resource}: {message})")


class DatabaseError(BaseError):
    def __init__(self, message: str, resource: str) -> None:
        super().__init__(f"[Database] ({resource}): {message}")


class PasswordHashError(BaseError):
    def __init__(self, message: str, resource: str) -> None:
        super().__init__(f"[PasswordHash] ({resource}): {message}")
