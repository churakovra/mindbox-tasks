from fastapi import FastAPI

from task2.app.controllers import set_routers

app = FastAPI()

set_routers(app)