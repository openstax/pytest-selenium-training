import pypom

from selenium.webdriver.common.by import By

from pages.search_results import SearchResults


class Browse(pypom.Page):
    # PyPOM uses this along with base_url to complete the url of the page.
    URL_TEMPLATE = '/browse'

    # Create a tuple containing the By function and locator name
    _main_content_locator = (By.ID, 'main-content')
    _search_input_locator = (By.ID, 'find-content-input')
    _search_category_locator = (By.CLASS_NAME, "search-category")

    @property
    def loaded(self):
        return self.is_element_displayed(
            *self._main_content_locator) and len(self.search_category_list) > 0

    @property
    def search_input(self):
        return self.find_element(*self._search_input_locator)

    @property
    def search_category_list(self):
        return self.find_elements(*self._search_category_locator)

    def search(self, query):
        self.search_input.send_keys(query)
        from selenium.webdriver.common.keys import Keys

        self.search_input.send_keys(Keys.ENTER)
        return SearchResults(self.driver, self.base_url).wait_for_page_to_load()
