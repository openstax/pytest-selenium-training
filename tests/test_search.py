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
