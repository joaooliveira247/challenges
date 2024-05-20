from bson import Decimal128
from decimal import Decimal
from typing import Any


def to_decimal(v: Any) -> Decimal128:
    return Decimal128(Decimal(str(v)))
