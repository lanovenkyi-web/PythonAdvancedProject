from pydantic import BaseModel


class Address(BaseModel):
     country: str
     city: str
     street: str
     home: int
     post_code: str


class User(BaseModel):
     id: int
     name: str
     age: int
     is_active: bool
     address: Address


address = Address(
     country="Poland",
     city="Legnica",
     street="Pomorska",
     home=52,
     post_code="59-220"
)


user = User(
     id=1,
     name="Serega",
     age=37,
     is_active=True,
     address=address
)


print(user)

print(user.address)
