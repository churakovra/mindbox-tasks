from fastapi import APIRouter

from task2.app.controllers.get_all_stuff_from_db import get_all_stuff_from_db
from task2.app.models.all_stuff import AllStuff

router = APIRouter()


@router.get("/all_stuff", response_model=AllStuff)
async def get_all_stuff_controller() -> list[AllStuff]:
    all_stuff = await get_all_stuff_from_db()
    return all_stuff
