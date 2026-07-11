import time

from scraper.rate_limiter import RateLimiter

limiter = RateLimiter(delay=1)

start = time.time()

for i in range(3):
    limiter.wait("https://www.amazon.in/product")
    print(f"Request {i+1}: {time.time() - start:.2f}s")