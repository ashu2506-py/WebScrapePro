from pathlib import Path

from alerts.email_service import EmailService
from database.models import AlertConfig, Product
from utils.logger import logger

class AlertEngine:

    def __init__(self, db):
        self.db = db
        self.email_service = EmailService()

    def check_alerts(self):

        alerts = self.db.query(AlertConfig).all()

        logger.info(f"Found {len(alerts)} alerts")

        for alert in alerts:

            logger.info("-" * 40)
            logger.info(f"Alert ID: {alert.id}")

            product = (
                self.db.query(Product)
                .filter(Product.id == alert.product_id)
                .first()
            )

            if product is None:
                logger.info("Product not found")
                continue

            logger.info(f"Product: {product.name}")
            logger.info(f"Current Price : {product.current_price}")
            logger.info(f"Target Price  : {alert.target_price}")

            if product.current_price <= alert.target_price:

                logger.info("Condition Matched ✅")

                html = f"""
                <h2>Price Alert</h2>

                <p>{product.name}</p>

                <p>Current Price: ₹{product.current_price}</p>
                """

                logger.info("Sending email...")

                self.email_service.send_email(
                    receiver_email=alert.email,
                    subject="Price Drop Alert",
                    html_body=html,
                )

                logger.info("Email sent!")

            else:

                logger.info("Condition Failed ❌")