from scraper.adapters.amazon import AmazonScraper
from scraper.adapters.flipkart import FlipkartScraper
from scraper.adapters.ebay import EbayScraper


def test_amazon_scraper():

    scraper = AmazonScraper()

    soup = scraper.load_local_html("mock_sites/amazon.html")

    product = scraper.extract_product_data(soup)

    assert product["price"] > 0


def test_flipkart_scraper():

    scraper = FlipkartScraper()

    soup = scraper.load_local_html("mock_sites/flipkart.html")

    product = scraper.extract_product_data(soup)

    assert product["price"] > 0


def test_ebay_scraper():

    scraper = EbayScraper()

    soup = scraper.load_local_html("mock_sites/ebay.html")

    product = scraper.extract_product_data(soup)

    assert product["price"] > 0