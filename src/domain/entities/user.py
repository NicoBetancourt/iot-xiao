from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    _id: Optional[str]
    name: str
    email: str
    dispoInfo: str
