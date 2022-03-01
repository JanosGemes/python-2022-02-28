import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
#given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #when
    driver.get("https://janosgemes.github.io/python-2022-02-28/")
    return driver


def test_welcome_page_header(driver):
    #then
    header = driver.find_element(By.TAG_NAME, "h1").text
    assert header == "Welcome"

def test_welcome_page_paragraph(driver):
    #then
    paragraph = driver.find_element(By.TAG_NAME, "p").text
    assert paragraph == "Welcome to the Python training!"
    
