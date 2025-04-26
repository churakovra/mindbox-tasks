from sqlalchemy import Table, Column, Integer, ForeignKey

from ..database import metadata_obj

products_category = Table(
    "products_category",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("p_id", Integer, ForeignKey("product_list.id")),
    Column("c_id", Integer, ForeignKey("category_list.id"))
)