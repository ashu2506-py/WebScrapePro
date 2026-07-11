import time
from urllib.parse import urlparse


class RateLimiter:
    """
    Enforces a minimum delay between requests to the same domain.
    """

    def __init__(self, delay=1.0):
        self.delay = delay
        self.last_request_time = {}

    def wait(self, url: str):
        """
        Wait if another request to the same domain was made recently.
        """
        domain = urlparse(url).netloc

        current_time = time.time()

        last_time = self.last_request_time.get(domain)

        if last_time is not None:
            elapsed = current_time - last_time

            if elapsed < self.delay:
                time.sleep(self.delay - elapsed)

        self.last_request_time[domain] = time.time()