# app/schemas/student.py

from pydantic import BaseModel
from typing import Optional

class CreateStudent(BaseModel):
    name: str
    matriculation_number: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    matriculation_number: Optional[str] = None
