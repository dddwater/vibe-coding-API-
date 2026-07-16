from pydantic import BaseModel
from typing import Optional

# Common fields shared across schemas
class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_year: Optional[int] = None
    price: Optional[float] = None

# Schema used when creating a book
class BookCreate(BookBase):
    pass

# Schema used when updating a book
class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None

# Schema used when returning a book from API
class Book(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }
