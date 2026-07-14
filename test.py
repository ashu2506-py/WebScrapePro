from sqlalchemy import text

from database.db import SessionLocal
from database.models import (
    AlertConfig,
    PriceHistory,
    Product,
    Site,
)

db = SessionLocal()

print("Deleting alerts...")
db.query(AlertConfig).delete()

print("Deleting price history...")
db.query(PriceHistory).delete()

print("Deleting products...")
db.query(Product).delete()

print("Deleting sites...")
db.query(Site).delete()

db.commit()

# Reset SQLite AUTOINCREMENT counters
db.execute(text("DELETE FROM sqlite_sequence WHERE name='alert_configs'"))
db.execute(text("DELETE FROM sqlite_sequence WHERE name='price_history'"))
db.execute(text("DELETE FROM sqlite_sequence WHERE name='products'"))
db.execute(text("DELETE FROM sqlite_sequence WHERE name='sites'"))

db.commit()

print("\n✅ Database reset successfully!")
print("All tables cleared.")
print("Auto-increment IDs reset.")

db.close()