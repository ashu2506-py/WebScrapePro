from alerts.alert_engine import AlertEngine
from database.db import SessionLocal


def test_scheduler_engine():

    db = SessionLocal()

    engine = AlertEngine(db)

    assert engine is not None

    db.close()