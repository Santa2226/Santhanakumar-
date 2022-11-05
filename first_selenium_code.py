from selenium import webdriver


# open a Firefox browser in python selenium
def test_Firefox(url):
    driver = webdriver.Firefox()
    return driver.get(url)


#  open a Chrome browser in python selenium
def test_chrome(url):
    driver = webdriver.Chrome()
    return driver.get(url)


#  open edge browser in python selenium
def test_edge(url):
    driver = webdriver.Edge()
    return driver.get(url)


url = "https://www.youtube.com"

test_edge(url)
