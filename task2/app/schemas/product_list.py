from sqlalchemy import Table, Column, Integer, String

from ..database import metadata_obj

product_list = Table(
    "product_list",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)