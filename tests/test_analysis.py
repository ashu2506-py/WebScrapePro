from analysis.trends import TrendAnalyzer
from database.db import SessionLocal
from database.models import Product


def test_highest_price():

    db = SessionLocal()

    analyzer = TrendAnalyzer(db)

    product = db.query(Product).first()

    highest = analyzer.get_highest_price(product.id)

    assert highest >= product.current_price

    db.close()


def test_moving_average():

    db = SessionLocal()

    analyzer = TrendAnalyzer(db)

    product = db.query(Product).first()

    avg = analyzer.get_moving_average(product.id, 7)

    assert avg > 0

    db.close()


def test_price_history():

    db = SessionLocal()

    analyzer = TrendAnalyzer(db)

    product = db.query(Product).first()

    history = analyzer.get_price_history(product.id)

    assert len(history) >= 30

    db.close()