from database.db import SessionLocal
from database.crud import create_site, create_product


class ScrapeManager:

    def __init__(self):
        self.db = SessionLocal()

    def save_product(self, product_data):

        site = create_site(
            db=self.db,
            name=product_data["site"],
            base_url=product_data["url"],
        )

        product = create_product(
            db=self.db,
            site=site,
            name=product_data["name"],
            product_url=product_data["url"],
            current_price=product_data["price"],
        )

        return product

    def close(self):
        self.db.close()