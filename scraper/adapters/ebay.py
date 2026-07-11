from scraper.base_scraper import BaseScraper


class EbayScraper(BaseScraper):

    def extract_product_data(self, soup, url="mock://ebay"):

        title = soup.find("h2", class_="item-title").get_text(strip=True)

        price = soup.find("span", class_="item-price").get_text(strip=True)

        price = (
            price.replace("$", "")
                 .replace(",", "")
                 .strip()
        )

        return {
            "name": title,
            "price": float(price),
            "url": url,
            "site": "eBay"
        }