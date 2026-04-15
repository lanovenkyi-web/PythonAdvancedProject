from pydantic import BaseModel
from typing import Optional


# OopCompanion:suppressRename


class CategoryBase(BaseModel):
    name: str

    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass




class CategoryResponse(CategoryBase):

    id: int

    model_config = {"from_attributes": True}


class QuestionBase(BaseModel):
    text: str
    answer: str


class QuestionCreate(QuestionBase):
    category_id: int




class QuestionResponse(QuestionBase):
    id: int
    category_id: int
    category: Optional[CategoryResponse] = None

    model_config = {"from_attributes": True}