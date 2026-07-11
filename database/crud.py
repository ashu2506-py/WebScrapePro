from sqlalchemy.orm import Session

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
    Create a product if it doesn't exist.
    If it exists, update its current price.
    """

    product = (
        db.query(Product)
        .filter(Product.product_url == product_url)
        .first()
    )

    if product:

        product.current_price = current_price

        db.commit()
        db.refresh(product)

        return product

    product = Product(
        name=name,
        product_url=product_url,
        current_price=current_price,
        site_id=site.id,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product