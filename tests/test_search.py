import random
from string import digits, ascii_letters
from time import sleep

import pytest

from pages.browse import Browse


@pytest.mark.nondestructive
def test_search_query_in_url(selenium, base_url):

    # Open the page
    browse = Browse(selenium, base_url).open()

    # Submit query for search
    query = 'Biology'
    browse.search(query)

    # Make an assertion that Biology is in the current url
    assert 'q=Biology' in selenium.current_url


@pytest.mark.nondestructive
def test_search_returns_no_results_and_message_displayed(selenium, base_url):

    # Open the page
    browse = Browse(selenium, base_url).open()

    # Create a string of random letters and numbers    # Submit query for search
    query = ''.join(random.choice(digits + ascii_letters) for i in range(32))
    search_results = browse.search(query)

    # Make sure we have no results and no result text is correct.
    assert search_results.has_no_results
    assert search_results.no_result_text == "No results found. Please try expanding your search."
