"""Pydantic model demo: nested model, validator, and JSON round-trip."""

from pydantic import BaseModel, field_validator


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

    @field_validator("zip_code")
    @classmethod
    def zip_must_be_five_digits(cls, v: str) -> str:
        if not v.isdigit() or len(v) != 5:
            raise ValueError("zip_code must be exactly 5 digits")
        return v


class Person(BaseModel):
    name: str
    age: int
    address: Address

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v < 0:
            raise ValueError("age must be non-negative")
        return v


def round_trip_json(json_str: str) -> str:
    """Parse JSON into a model, then serialize back to JSON."""
    person = Person.model_validate_json(json_str)
    return person.model_dump_json(indent=2)


if __name__ == "__main__":
    original = """{
  "name": "Ada Lovelace",
  "age": 36,
  "address": {
    "street": "10 Downing St",
    "city": "London",
    "zip_code": "12345"
  }
}"""

    print("Original JSON:")
    print(original)
    print()

    result = round_trip_json(original)
    print("After round-trip:")
    print(result)
    print()

    # Verify round-trip preserves data
    assert Person.model_validate_json(original) == Person.model_validate_json(result)
    print("Round-trip successful: parsed models are equal.")
