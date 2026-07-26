from sqlalchemy import create_engine


def get_engine():
    return create_engine(
    "postgresql://trade_admin:trade_password@localhost:5433/trade_db"
)