from sqlalchemy.orm import Session

from database.models import PriceHistory
from datetime import datetime, timedelta


class TrendAnalyzer:

    def __init__(self, db: Session):
        self.db = db

    def get_price_history(self, product_id: int):

        return (
            self.db.query(PriceHistory)
            .filter(PriceHistory.product_id == product_id)
            .order_by(PriceHistory.recorded_at)
            .all()
        )
    
    def get_current_price(self, product_id: int):

        history = self.get_price_history(product_id)

        if not history:
            return None

        return history[-1].price

    def get_lowest_price(self, product_id: int):

        history = self.get_price_history(product_id)

        if not history:
            return None

        return min(record.price for record in history)
    
    def get_highest_price(self, product_id: int):

        history = self.get_price_history(product_id)

        if not history:
            return None

        return max(record.price for record in history)
    
    def get_moving_average(self, product_id: int, days: int):
        cutoff_date = datetime.utcnow() - timedelta(days=days)

        history = (
            self.db.query(PriceHistory)
            .filter(
                PriceHistory.product_id == product_id,
                PriceHistory.recorded_at >= cutoff_date,
            )
            .all()
        )

        if not history:
            return None

        prices = [record.price for record in history]

        return round(sum(prices) / len(prices), 2)
    
    def get_price_change(self, product_id: int):

        history = self.get_price_history(product_id)

        if len(history) < 2:
            return None

        old_price = history[0].price
        new_price = history[-1].price

        difference = new_price - old_price

        percentage = (difference / old_price) * 100

        return {
            "difference": round(difference, 2),
            "percentage": round(percentage, 2),
        }
        
    def get_trend(self, product_id: int):

        change = self.get_price_change(product_id)

        if change is None:
            return "Not enough data"

        if change["difference"] > 0:
            return "Increasing"

        elif change["difference"] < 0:
            return "Decreasing"

        return "Stable"