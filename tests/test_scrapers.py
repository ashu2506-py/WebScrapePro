from scraper.adapters.amazon import AmazonScraper


def test_amazon_scraper():

    scraper = AmazonScraper()

    soup = scraper.load_local_html(
        "mock_sites/amazon.html"
    )

    product = scraper.extract_product_data(soup)

    assert product["name"] != ""

    assert product["price"] > 0