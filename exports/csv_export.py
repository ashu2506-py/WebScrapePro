import csv
import os
from datetime import datetime

from database.models import PriceHistory


class CSVExporter:

    def __init__(self):
        os.makedirs("exports", exist_ok=True)

    def export_price_history(self, db, product):

        history = (
            db.query(PriceHistory)
            .filter(PriceHistory.product_id == product.id)
            .order_by(PriceHistory.recorded_at)
            .all()
        )

        filename = (
            f"exports/{product.name.replace(' ', '_')}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Product",
                "Price",
                "Date"
            ])

            for record in history:

                writer.writerow([
                    product.name,
                    record.price,
                    record.recorded_at
                ])

        return filename