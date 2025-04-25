from sqlalchemy import Table, Column, Integer, String

from task2.app.database import metadata_obj

category_list = Table(
    "category_list",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)