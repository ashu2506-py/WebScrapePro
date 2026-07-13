from database.db import SessionLocal
from database.models import Product


def test_database_connection():

    db = SessionLocal()

    products = db.query(Product).all()

    assert products is not None

    db.close()