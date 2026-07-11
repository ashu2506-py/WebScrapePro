from database.db import SessionLocal
from database.crud import create_site, create_product

db = SessionLocal()

site = create_site(
    db,
    "Amazon",
    "https://amazon.in"
)

product = create_product(
    db=db,
    site=site,
    name="Apple iPhone 16 Pro",
    product_url="https://amazon.in/iphone16pro",
    current_price=119999
)

print(product.id)
print(product.name)
print(product.current_price)