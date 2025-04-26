from ..models.all_stuff import AllStuff
from sqlalchemy import Connection, text


async def get_all_stuff_from_db(connection: Connection) -> list[AllStuff]:
    pass
