from scraper.retry import retry

counter = 0


@retry(max_attempts=4)
def demo():

    global counter

    counter += 1

    print(f"Attempt {counter}")

    if counter < 4:
        raise Exception("Temporary Error")

    return "Success"


print(demo())