from database.db import SessionLocal
from analysis.trends import TrendAnalyzer

db = SessionLocal()

analyzer = TrendAnalyzer(db)

history = analyzer.get_price_history(1)

for record in history:
    print(record.price, record.recorded_at)

print("Current Price:", analyzer.get_current_price(1))

print("Lowest Price:", analyzer.get_lowest_price(1))

print("Highest Price:", analyzer.get_highest_price(1))

print("7-Day Average :", analyzer.get_moving_average(1, 7))
print("30-Day Average:", analyzer.get_moving_average(1, 30))

print(analyzer.get_price_change(1))
print("Trend :", analyzer.get_trend(1))

db.close()