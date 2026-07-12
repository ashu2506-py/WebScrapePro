from sqlalchemy.orm import Session
from datetime import datetime

from database.models import (
    Site,
    Product,
    PriceHistory,
    AlertConfig,
)

def create_site(
    db: Session,
    name: str,
    base_url: str,
):
    
    
    """
    Create a new shopping site.
    """

    existing = (
        db.query(Site)
        .filter(Site.name == name)
        .first()
    )

    if existing:
        return existing

    site = Site(
        name=name,
        base_url=base_url,
    )

    db.add(site)
    db.commit()
    db.refresh(site)

    return site




def create_product(
    db: Session,
    site: Site,
    name: str,
    product_url: str,
    current_price: float,
):
    """
    Create or update a product and maintain price history.
    """

    product = (
        db.query(Product)
        .filter(Product.product_url == product_url)
        .first()
    )

    if product:

        # Update only if price changed
        if product.current_price != current_price:

            product.current_price = current_price
            product.last_updated = datetime.utcnow()

            db.commit()
            db.refresh(product)

            add_price_history(
                db=db,
                product=product,
                price=current_price
            )

        return product

    product = Product(
        name=name,
        product_url=product_url,
        current_price=current_price,
        site_id=site.id,
        last_updated=datetime.utcnow(),
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    add_price_history(
        db=db,
        product=product,
        price=current_price
    )

    return product


def add_price_history(
    db: Session,
    product: Product,
    price: float,
):
    """
    Add a price history record only if the price changed.
    """

    latest = (
        db.query(PriceHistory)
        .filter(PriceHistory.product_id == product.id)
        .order_by(PriceHistory.recorded_at.desc())
        .first()
    )

    if latest and latest.price == price:
        return latest

    history = PriceHistory(
        product_id=product.id,
        price=price,
        recorded_at=datetime.utcnow()
    )

    db.add(history)
    db.commit()
    db.refresh(history)

    return history