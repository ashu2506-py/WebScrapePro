from database.db import SessionLocal
from database.models import Product, Site


def test_database_connection():

    db = SessionLocal()

    assert db is not None

    db.close()


def test_products_exist():

    db = SessionLocal()

    products = db.query(Product).all()

    assert len(products) >= 20

    db.close()


def test_sites_exist():

    db = SessionLocal()

    sites = db.query(Site).all()

    assert len(sites) >= 3

    db.close()