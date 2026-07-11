from scraper.adapters.amazon import AmazonScraper
from scraper.adapters.flipkart import FlipkartScraper
from scraper.adapters.ebay import EbayScraper


class ScraperFactory:

    SCRAPERS = {
        "amazon": AmazonScraper,
        "flipkart": FlipkartScraper,
        "ebay": EbayScraper,
    }

    @classmethod
    def get_scraper(cls, site):

        scraper = cls.SCRAPERS.get(site.lower())

        if scraper is None:
            raise ValueError(f"Unsupported site: {site}")

        return scraper()