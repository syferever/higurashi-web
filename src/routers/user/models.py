from sqlmodel import SQLModel, Field


class User(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False)
