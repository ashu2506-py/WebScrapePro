from abc import ABC, abstractmethod
from scraper.user_agents import get_random_user_agent
from bs4 import BeautifulSoup
import requests


class BaseScraper(ABC):

    def __init__(self, headers=None, timeout=10):
        self.headers = headers or get_random_user_agent()
        self.timeout = timeout

    def fetch_page(self, url):

        response = requests.get(
            url,
            headers=self.headers,
            timeout=self.timeout
        )

        response.raise_for_status()

        return BeautifulSoup(response.text, "lxml")

    def load_local_html(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:
            html = file.read()

        return BeautifulSoup(html, "lxml")

    @abstractmethod
    def extract_product_data(self, soup, url):
        pass