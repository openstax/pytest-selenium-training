import random
from string import digits, ascii_letters
from time import sleep

import pytest

from pages.browse import Browse


@pytest.mark.nondestructive
def test_search_query_in_url(selenium, base_url):

    # Open the page
    browse = Browse(selenium, base_url).open()

    # Allow the page to load
    sleep(3)

    # Submit query for search
    query = 'Biology'
    browse.search(query)

    # Make an assertion that Biology is in the current url
    assert 'q=Biology' in selenium.current_url


@pytest.mark.nondestructive
def test_search_returns_no_results_and_message_displayed(selenium, base_url):

    # Open the page
    browse = Browse(selenium, base_url).open()

    # Allow page to load
    sleep(3)

    # Create a string of random letters and numbers    # Submit query for search
    query = ''.join(random.choice(digits + ascii_letters) for i in range(32))
    browse.search(query)

    # Allow enough time for results to display
    sleep(3)

    # Make sure we have no results and no result text is correct.
    assert browse.has_no_results
    assert browse.no_result_text == "No results found. Please try expanding your search."
