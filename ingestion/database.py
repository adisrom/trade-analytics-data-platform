from sqlalchemy import create_engine
from ingestion.config import POSTGRES_CONFIG


def get_engine():
    """
    Creates a connection engine to PostgreSQL.
    """

    connection_string = (
        f"postgresql://{POSTGRES_CONFIG['user']}:"
        f"{POSTGRES_CONFIG['password']}@"
        f"{POSTGRES_CONFIG['host']}:"
        f"{POSTGRES_CONFIG['port']}/"
        f"{POSTGRES_CONFIG['database']}"
    )

    engine = create_engine(connection_string)

    return engine