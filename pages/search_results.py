from selenium.webdriver.common.by import By

import pypom


class SearchResults(pypom.Page):
    URL_TEMPLATE = "/search?q={q}"

    _num_results_span_locator = (
        By.CSS_SELECTOR,
        'span[data-l10n-id="search-results-number-results"]',
    )
    _no_results_text_locator = (
        By.CSS_SELECTOR,
        '#results p[data-l10n-id="search-results-list-no-results"]',
    )
    _results_locator = (By.CSS_SELECTOR, "#results table.table tbody tr")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._num_results_span_locator)

    @property
    def results(self):
        return self.find_elements(*self._results_locator)

    @property
    def has_no_results(self):
        return len(self.results) == 0

    @property
    def no_result_text(self):
        return self.find_element(*self._no_results_text_locator).text
