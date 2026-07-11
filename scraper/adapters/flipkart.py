from scraper.base_scraper import BaseScraper


class FlipkartScraper(BaseScraper):

    def extract_product_data(self, soup, url="mock://flipkart"):

        title = soup.find("h1", class_="title").get_text(strip=True)

        price = soup.find("div", class_="price").get_text(strip=True)

        price = (
            price.replace("₹", "")
                 .replace(",", "")
                 .strip()
        )

        return {
            "name": title,
            "price": float(price),
            "url": url,
            "site": "Flipkart"
        }