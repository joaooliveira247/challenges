import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class AccountBaseSchema(BaseModel):
    full_name: str = Field(
        ...,
        description="Full name of the account owner.",
        min_length=3,
        max_length=255,
    )
    email: EmailStr = Field(..., description="Email account owner.")
    ssn: str = Field(
        ...,
        description="Brazilian CPF identification",
        max_length=11,
        min_length=11,
        examples=["1234567810"]
    )

    @field_validator("ssn")
    def validate_ssn(cls, value: str) -> str:
        cpf = re.sub(r"\D", "", value)

        if cpf == cpf[0] * 11:
            raise ValueError("Invalid CPF")

        # first digit
        sum_ = sum(int(cpf[i]) * (10 - i) for i in range(9))
        first_digit = (sum_ * 10 % 11) % 10

        # second digit
        sum_ = sum(int(cpf[i]) * (11 - i) for i in range(10))
        second_digit = (sum_ * 10 % 11) % 10

        if cpf[-2:] != f"{first_digit}{second_digit}":
            raise ValueError("Invalid CPF")

        return cpf


class PasswordMixin(BaseModel):
    password: str = Field(
        ...,
        description="Account password",
        min_length=8,
        max_length=128,
        examples=["Hello@124"],
    )

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        pattern = {
            "lower": r"[a-z]",
            "upper": r"[A-Z]",
            "digit": r"\d",
            "special": r"[@$!%*?&]",
        }

        components = {
            key: "".join(re.findall(regex, value)) or None
            for key, regex in pattern.items()
        }

        missing_components = [
            key for key, value in components.items() if value is None
        ]

        if missing_components:
            raise ValueError(
                f"Wrong password format! characters missing: {', '.join(missing_components)}"
            )

        return value


class AccountInSchema(AccountBaseSchema, PasswordMixin): ...
