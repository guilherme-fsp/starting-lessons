from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FetchTick:
    def fetch_status_data(self):
        self.user_text = input("Digite o codigo B3: ")  # Get the stock code


class SearchRoutine:
    def setup_method(self):
        self.driver = webdriver.Firefox()  # Initialize the Firefox WebDriver
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()  # Quit the WebDriver

    def search_routine(self, user_text):
        self.driver.get("https://www.investing.com/")
        self.driver.set_window_size(1365, 880)

        # Wait for the search bar to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "*[data-test=\"search-section\"]"))
        )
        search_box = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"search-section\"]")
        search_box.click()
        search_box.send_keys(user_text)
        search_box.send_keys(Keys.RETURN)  # Simulate Enter key

        # Wait for the search results to load and click the first result
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".mainSearch_symbol__YMUvc"))
        ).click()


# Usage
fetcher = FetchTick()
fetcher.fetch_status_data()  # Get user input

searcher = SearchRoutine()
searcher.setup_method()  # Initialize the browser

try:
    searcher.search_routine(fetcher.user_text)  # Pass user_text to the search routine
finally:
    searcher.teardown_method()  # Ensure browser quits properly