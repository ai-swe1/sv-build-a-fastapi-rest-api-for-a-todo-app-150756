import os
from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")
# connect_args needed for SQLite when using multiple threads
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def init_db() -> None:
    """Create database tables if they don't exist."""
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_db() -> Session:
    """Yield a SQLModel session and ensure it is closed after use."""
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
