from pydantic import BaseModel, Field

class ExampleModel(BaseModel):
    name:str = Field(description="Name of thing")
    number:int = Field(description="Number of thing", ge=0)