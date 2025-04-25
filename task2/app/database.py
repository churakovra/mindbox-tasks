from sqlalchemy import create_engine

from task2.app.config.preferences import DATABASE_URL

engine = create_engine(url=DATABASE_URL)
