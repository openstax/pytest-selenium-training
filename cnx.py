from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_search_query_in_url(driver, base_url):

    # Bring up the page specified by the base_url
    driver.get(base_url)

    # Allow the page to load
    sleep(3)

    # Find the search input box and enter Biology and submit
    search_box = driver.find_element_by_id('find-content-input')
    search_box.send_keys('Biology')
    search_box.send_keys(Keys.ENTER)

    # Make an assertion that Biology is in the current url
    try:
        assert 'q=Biology' in driver.current_url
    except AssertionError:
        return 'Failed'

    # Close down the browser
    driver.quit()

    return 'Passed'


if __name__ == '__main__':

    # Create an instance of selenium web driver
    driver = webdriver.Chrome()

    # Run our first test!
    result = test_search_query_in_url(driver, 'https://cnx.org/browse')

    print(f'The test {result}!')
