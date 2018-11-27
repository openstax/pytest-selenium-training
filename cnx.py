from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    # Create an instance of selenium web driver
    driver = webdriver.Chrome()

    # Bring up the main cnx.org website
    driver.get('https://cnx.org')

    sleep(3)

    # Find the link to visit the search page
    search_button = driver.find_element_by_css_selector('#page-nav #nav-browse a')

    # Slow things down a bit
    sleep(2)

    # Click the link
    search_button.click()

    # Let the user see what is happening
    sleep(5)

    search_box = driver.find_element_by_id('find-content-input')
    search_box.send_keys('Biology')

    # Let the user see something
    sleep(2)

    # Submit the query
    search_box.send_keys(Keys.ENTER)

    # zzzzzz
    sleep(5)

    # Close down the browser
    driver.quit()
