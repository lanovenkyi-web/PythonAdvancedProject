from decimal import Decimal
from pydantic import BaseModel, ConfigDict

#TODO: Task 2

class MineralOutput(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    id: int
    name: str
    color: str
    solid: Decimal

mineral = { "id": 3, "name": 'gold', "color": 'yellow', "solid": 1234.4}

resp = MineralOutput.model_validate(mineral)
print(resp)