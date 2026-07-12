from datetime import datetime, timedelta

from database.db import SessionLocal
from database.models import Site, Product, PriceHistory
from mock_data import products

db = SessionLocal()


def get_or_create_site(name, url):
    site = db.query(Site).filter(Site.name == name).first()

    if site:
        return site

    site = Site(
        name=name,
        base_url=url
    )

    db.add(site)
    db.commit()
    db.refresh(site)

    return site


for item in products:

    print(f"Adding {item['name']}")

    site = get_or_create_site(
        item["site"],
        item["url"]
    )

    product = (
        db.query(Product)
        .filter(Product.product_url == item["url"])
        .first()
    )

    if product:
        db.query(PriceHistory).filter(
            PriceHistory.product_id == product.id
        ).delete()

        db.delete(product)
        db.commit()

    latest_price = item["prices"][-1]

    product = Product(
        name=item["name"],
        product_url=item["url"],
        current_price=latest_price,
        last_updated=datetime.utcnow(),
        site_id=site.id,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    total_days = len(item["prices"])

    for index, price in enumerate(item["prices"]):

        days_ago = total_days - index - 1

        history = PriceHistory(
            product_id=product.id,
            price=price,
            recorded_at=datetime.utcnow() - timedelta(days=days_ago)
        )

        db.add(history)

    db.commit()

print("\nDatabase populated successfully!")

db.close()