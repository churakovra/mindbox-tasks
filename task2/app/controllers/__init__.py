from fastapi import FastAPI
from .all_stuff import router as all_stuff_router

routers = [
    all_stuff_router
]

def set_routers(app: FastAPI):
    for router in routers:
        app.include_router(router)