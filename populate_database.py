import random
from datetime import datetime, timedelta

from database.db import SessionLocal
from database.models import Site, Product, PriceHistory
from mock_data import products

# Keeps generated prices the same every time you run the script
random.seed(42)

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


def generate_price_history(base_price, days=30):
    """
    Generate realistic price history for the last 'days' days.
    Prices fluctuate within a reasonable range.
    """

    prices = []
    current_price = base_price

    for _ in range(days):

        # Daily fluctuation between -2.5% and +2.5%
        change = random.uniform(-0.025, 0.025)

        current_price *= (1 + change)

        # Prevent unrealistic values
        current_price = max(current_price, base_price * 0.70)
        current_price = min(current_price, base_price * 1.15)

        prices.append(round(current_price, 2))

    return prices


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

    # Generate 30 days of prices
    prices = generate_price_history(
        item["base_price"],
        days=30
    )

    latest_price = prices[-1]

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

    total_days = len(prices)

    for index, price in enumerate(prices):

        days_ago = total_days - index - 1

        history = PriceHistory(
            product_id=product.id,
            price=price,
            recorded_at=datetime.utcnow() - timedelta(days=days_ago)
        )

        db.add(history)

    db.commit()

print("\n✅ Database populated successfully!")
print(f"Products inserted: {len(products)}")
print(f"Price history records: {len(products) * 30}")

db.close()