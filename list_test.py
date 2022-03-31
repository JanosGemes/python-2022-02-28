import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
#given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #when
    driver.get("http://127.0.0.1:5500/docs/index.html")
    return driver


def test_list_items(driver: webdriver.Chrome):
    elements = driver.find_elements(By.TAG_NAME, "li")
    list_items = []
    for element in elements:
        list_items.append(element.text) 
    assert list_items == ["Phyton","pip","webdriver", "Selenium" ]

def test_table_cells(driver: webdriver.Chrome):
    elements = driver.find_elements_by_class_name("price")
    list_items = []
    for element in elements:
        list_items.append(int(element.text)) 
    assert list_items == [100, 400, 150]

def test_checkbox(driver: webdriver.Chrome):
    CheckBox = driver.find_element_by_name("accept-licence")
    CheckBox.click()
    print("End")

def test_select(driver: webdriver.Chrome):
    select = Select(driver.find_element_by_name("car-type"))
    select.select_by_visible_text("opel")
    CheckBox.click()
    print("End")