import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from apscheduler.schedulers.blocking import BlockingScheduler

from database.db import SessionLocal
from alerts.alert_engine import AlertEngine
from utils.logger import logger
from scraper.scraper_runner import ScraperRunner

db = SessionLocal()

engine = AlertEngine(db)

scheduler = BlockingScheduler()

def check_prices():

    print("=" * 60)

    print("Running Scrapers...")

    ScraperRunner().run()

    print("Checking Alerts...")

    engine.check_alerts()

    print("Finished")

    print("=" * 60)


scheduler.add_job(
    check_prices,
    trigger="interval",
    seconds=10
)

logger.info("Scheduler started...")

try:
    scheduler.start()

except (KeyboardInterrupt, SystemExit):

    logger.info("Scheduler stopped.")
    db.close()