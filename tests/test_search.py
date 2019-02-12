import random
from string import digits, ascii_letters
from time import sleep

import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.nondestructive
def test_search_query_in_url(selenium, base_url):

    # Bring up the page specified by the base_url
    selenium.get(f'{base_url}/browse')

    # Allow the page to load
    sleep(3)

    # Find the search input box and enter Biology and submit
    search_box = selenium.find_element_by_id('find-content-input')
    search_box.send_keys('Biology')
    search_box.send_keys(Keys.ENTER)

    # Make an assertion that Biology is in the current url
    assert 'q=Biology' in selenium.current_url


@pytest.mark.nondestructive
def test_search_returns_no_results_and_message_displayed(selenium, base_url):

    # Bring up the page specified by the base_url
    selenium.get(f'{base_url}/browse')

    # Allow page to load
    sleep(3)

    # Create a string of random letters and numbers
    query = ''.join(random.choice(digits + ascii_letters) for i in range(32))

    # Find the search input box and enter the query and submit
    search_box = selenium.find_element_by_id('find-content-input')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    # Allow enough time for results to display
    sleep(3)

    # Results are shown in a table element. Find all table rows.
    result_items = selenium.find_elements_by_css_selector(
        '#results table.table tbody tr')

    # When no results are found a message is displayed. Find the message.
    result_text = selenium.find_element_by_css_selector(
        '#results p[data-l10n-id="search-results-list-no-results"]').text

    assert len(result_items) == 0
    assert result_text == "No results found. Please try expanding your search."
