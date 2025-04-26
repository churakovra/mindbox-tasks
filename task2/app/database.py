from sqlalchemy import create_engine, URL, MetaData

from .config.preferences import *

db_url = URL.create(
    drivername="postgresql",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

engine = create_engine(url=db_url)

metadata_obj = MetaData()
