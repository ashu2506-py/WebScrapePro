import os

from database.db import SessionLocal
from database.models import Product
from exports.csv_export import CSVExporter


def test_csv_export():

    db = SessionLocal()

    product = db.query(Product).first()

    exporter = CSVExporter()

    filename = exporter.export_price_history(
        db,
        product
    )

    assert os.path.exists(filename)

    db.close()