from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://todos:OxVEHPm7ZtKrquKuxwLPGXH46GYDVhWY@dpg-cgnuu4l269v5rj8qpp40-a.singapore-postgres.render.com/todos_v42e"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
