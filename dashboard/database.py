import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_engine():

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")

    connection_string = (
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )

    return create_engine(connection_string)