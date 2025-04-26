from fastapi import FastAPI

from .controllers import set_routers
from .database import init_db

app = FastAPI()

set_routers(app)

init_db()
