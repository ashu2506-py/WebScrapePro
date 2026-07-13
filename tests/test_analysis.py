from database.db import SessionLocal
from analysis.trends import TrendAnalyzer


def test_lowest_price():

    db = SessionLocal()

    analyzer = TrendAnalyzer(db)

    history = analyzer.get_price_history(1)

    if history:

        lowest = analyzer.get_lowest_price(1)

        assert lowest <= history[-1].price

    db.close()