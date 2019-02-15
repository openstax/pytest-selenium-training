import pypom

from selenium.webdriver.common.by import By


class Browse(pypom.Page):
    # PyPOM uses this along with base_url to complete the url of the page.
    URL_TEMPLATE = '/browse'

    # Create a tuple containing the By function and locator name
    _search_input_locator = (By.ID, 'find-content-input')
    _results_locator = (By.CSS_SELECTOR, '#results table.table tbody tr')
    _no_results_text_locator = (
        By.CSS_SELECTOR,
        '#results p[data-l10n-id="search-results-list-no-results"]'
    )

    @property
    def search_input(self):
        return self.find_element(*self._search_input_locator)

    @property
    def results(self):
        return self.find_elements(*self._results_locator)

    @property
    def has_no_results(self):
        return len(self.results) == 0

    @property
    def no_result_text(self):
        return self.find_element(*self._no_results_text_locator).text

    def search(self, query):
        self.search_input.send_keys(query)
        from selenium.webdriver.common.keys import Keys

        self.search_input.send_keys(Keys.ENTER)
        return
