from fastapi import FastAPI

from .controllers import set_routers

app = FastAPI()

set_routers(app)