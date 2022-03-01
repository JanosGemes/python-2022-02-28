from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:5500/docs/index.html")


def test_list_items(driver: webdriver.Chrome):
    elements = driver.find_elements(By.TAG_NAME, "li")
    list_items = []
    for element in elements:
        list_items.append(element.text) 
    assert list_items == ["Phyton","pip","webdriver", "Selenium"  ]