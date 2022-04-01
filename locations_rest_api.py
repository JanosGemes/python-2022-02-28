from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import uuid

def delete_all_locations():
    requests.delete("http://127.0.0.1:8080/api/locations")

def create_location(name_prefix, coords):
    name = name_prefix + " " + str(uuid.uuid4())
    data = {"name": name, "coords" : "5,5"}
    requests.post("http://127.0.0.1:8080/api/locations", json=data)