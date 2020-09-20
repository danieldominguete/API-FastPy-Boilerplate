from pydantic import BaseModel

class ExampleRequestBody(BaseModel):
    
    number1: float = 0
    number2: float = 0
    operator: str