from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Boolean
)

from sqlalchemy.orm import relationship
from datetime import datetime

from database.db import Base


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    base_url = Column(String, nullable=False)

    products = relationship("Product", back_populates="site")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    product_url = Column(String, unique=True, nullable=False)

    current_price = Column(Float, nullable=False)

    last_updated = Column(DateTime, default=datetime.utcnow)

    site_id = Column(Integer, ForeignKey("sites.id"))

    site = relationship("Site", back_populates="products")

    price_history = relationship(
        "PriceHistory",
        back_populates="product",
        cascade="all, delete"
    )

    alerts = relationship(
        "AlertConfig",
        back_populates="product",
        cascade="all, delete"
    )


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    price = Column(Float, nullable=False)

    recorded_at = Column(DateTime, default=datetime.utcnow)

    product = relationship(
        "Product",
        back_populates="price_history"
    )


class AlertConfig(Base):
    __tablename__ = "alert_configs"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    target_price = Column(Float, nullable=False)

    email = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)

    product = relationship(
        "Product",
        back_populates="alerts"
    )