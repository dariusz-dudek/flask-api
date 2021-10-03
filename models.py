from pydantic import BaseModel
from typing import Optional


class Author(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str


class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author_id: int
