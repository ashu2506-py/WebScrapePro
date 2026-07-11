import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def retry(max_attempts=3, backoff_factor=2):
    """
    Retry decorator with exponential backoff.

    Args:
        max_attempts (int): Maximum retry attempts.
        backoff_factor (int): Delay multiplier.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            delay = 1

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    logger.warning(
                        f"Attempt {attempt} failed: {e}"
                    )

                    if attempt == max_attempts:
                        logger.error(
                            "Maximum retry attempts reached."
                        )
                        raise

                    time.sleep(delay)

                    delay *= backoff_factor

        return wrapper

    return decorator