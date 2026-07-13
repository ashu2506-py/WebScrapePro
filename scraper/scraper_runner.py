from scraper.adapters.amazon import AmazonScraper
from scraper.adapters.flipkart import FlipkartScraper
from scraper.adapters.ebay import EbayScraper

from scraper.scrape_manager import ScrapeManager


class ScraperRunner:

    def __init__(self):
        self.manager = ScrapeManager()

    def run(self):

        scrapers = [
            (
                AmazonScraper(),
                "mock_sites/amazon.html"
            ),
            (
                FlipkartScraper(),
                "mock_sites/flipkart.html"
            ),
            (
                EbayScraper(),
                "mock_sites/ebay.html"
            ),
        ]

        for scraper, html_file in scrapers:

            soup = scraper.load_local_html(html_file)

            product = scraper.extract_product_data(soup)

            self.manager.save_product(product)

            print(f"Saved {product['name']}")

        self.manager.close()