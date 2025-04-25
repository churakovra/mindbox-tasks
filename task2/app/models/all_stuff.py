from pydantic import BaseModel

class AllStuff(BaseModel):
    product_name: str
    category_name: str
