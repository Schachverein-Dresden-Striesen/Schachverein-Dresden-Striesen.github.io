from __future__ import annotations

import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

LOGGER = logging.getLogger(__name__)


class ClubScraper:
    def __init__(self, club_url: str, login_url: str, username: str, password: str):
        self.club_url = club_url
        self.login_url = login_url
        self.username = username
        self.password = password

    def open_browser(self) -> webdriver.Firefox:
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        return driver

    def login(self, driver: webdriver.Firefox) -> None:
        if not self.username or not self.password:
            raise ValueError("DWZ_USERNAME and DWZ_PASSWORD must be set.")

        driver.get(self.login_url)
        driver.find_element(By.ID, "username").send_keys(self.username)
        driver.find_element(By.ID, "password").send_keys(self.password)
        driver.find_element(By.CSS_SELECTOR, ".submit").click()

    def fetch_club_page(self) -> str:
        driver = self.open_browser()
        try:
            self.login(driver)
            driver.get(self.club_url)
            return driver.page_source
        finally:
            driver.quit()

    def extract_player_links(self, page_source: str) -> list[str]:
        return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    LOGGER.info("Club scraper entry point")
