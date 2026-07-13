from database.db import SessionLocal
from database.crud import create_alert


def test_alert_creation():

    db = SessionLocal()

    alert = create_alert(
        db=db,
        product_name="Apple iPhone 16 Pro",
        email="test@example.com",
        target_price=100000
    )

    assert alert.email == "test@example.com"

    db.close()