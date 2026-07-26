import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.db.base import Base
from backend.db.database import get_db
from backend.main import app


# ------------------------------
# Test Database
# ------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(

    SQLALCHEMY_DATABASE_URL,

    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine,
)


@pytest.fixture(scope="session")

def setup_database():

    """
    Creates all tables before tests
    and removes them afterwards.
    """

    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db(setup_database):

    connection = TestingSessionLocal()

    # Clear database
    from backend.db.models.log import Log

    connection.query(Log).delete()

    connection.commit()

    try:

        yield connection

    finally:

        connection.close()

@pytest.fixture()

def client(db):

    """
    Returns a FastAPI TestClient
    using the testing database.
    """

    def override_get_db():

        yield db

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:

        yield test_client

    app.dependency_overrides.clear()