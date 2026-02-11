from pydantic import BaseModel, Field, model_validator, EmailStr, ValidationError


class Address(BaseModel):
    country: str = Field(min_length=2)
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)
    post_code: str


class User(BaseModel):
    name: str = Field(min_length=2, pattern="[A-Za-zА-Яа-яЁё]+")
    age: int = Field(ge=0, le=120)
    email: str = EmailStr()
    is_employed: bool
    address: Address

    @model_validator(mode="after")
    def check_age_for_employed(self) -> "User":
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError(
                "Если пользователь занят (is_employed=true), возраст должен быть не меньше 18 и не больше 65 лет")
        return self


address1 = Address(
    country="Poland",
    city="Legnica",
    street="Pomorska",
    house_number=52,
    post_code="59-220"
)

user1 = User(
    name="Serega",
    age=50,
    email="itshock@gmail.com",
    is_employed=True,
    address=address1
)

json_str = """{
     "name":"Serega",
     "age":37,
     "email":"itschok@gmail.com",
     "is_employed":true,
     "address":{"country":"Poland",
               "city":"Legnica",
               "street":"Pomorska", 
               "house_number":52,
               "post_code":"59-220"
               }
}"""

json_str2 = """{
    "name": "Alexandr",
    "age": 72,
    "email": "alex.dev@outlook.com",
  "is_employed": true,
  "address": {
         "country": "Germany",
         "city": "Berlin",
         "street": "Friedrichstrasse",
         "house_number": 101,
         "post_code": "10117"}
}"""


def get_json(js_str: str) -> str:
    try:
        user = User.model_validate_json(js_str)

        ret_json = user.model_dump_json()
        return ret_json
    except ValidationError as e:
        print(e)
        return "Ошибка валидации, введены не валидные значения"


print(get_json(json_str))
print(get_json(json_str2))
