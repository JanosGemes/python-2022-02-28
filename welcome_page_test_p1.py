from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_welcome_page_paragraph():
    #given
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #when
    driver.get("https://janosgemes.github.io/python-2022-02-28/")
    #then
    paragraph = driver.find_element(By.TAG_NAME, "p1").text
    assert paragraph == "Welcome to the Python training!"