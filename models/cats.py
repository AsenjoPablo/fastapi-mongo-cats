from typing import Optional, Union
from pydantic import BaseModel

class Cat(BaseModel):
    id: str | None = None
    name: str
    age: Union[int, float]
    breed: str
    image: Optional[str] | None = None
    vaccinations: list[dict]