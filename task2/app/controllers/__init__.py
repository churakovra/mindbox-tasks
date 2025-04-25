from fastapi import FastAPI

routers = [
    # all routers from controllers
]

def set_routers(app: FastAPI):
    for router in routers:
        app.include_router(router)