from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from database import create_db_and_tables

class User(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str 
    email : str = Field(index=True, unique=True)
    uploads : List["Upload"] = Relationship(back_populates="owner")
    
    
class Upload(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user_id")
    filename: str
    data: str
    owner: Optional[User] = Relationship(back_populates="uploads")
    
    
create_db_and_tables()