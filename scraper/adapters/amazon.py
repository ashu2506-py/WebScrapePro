from scraper.base_scraper import BaseScraper


class AmazonScraper(BaseScraper):

    def extract_product_data(self, soup, url="mock://amazon"):

        title = soup.find("span", id="productTitle").get_text(strip=True)

        price = soup.find("span", class_="a-price-whole").get_text(strip=True)

        price = float(price.replace(",", ""))

        return {
            "name": title,
            "price": price,
            "url": url,
            "site": "Amazon"
        }