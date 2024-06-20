from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
# from selenium.webdriver.common.by import By

from time import sleep
import sys
import os

from Utils import BAD_RETURN_CODE, GOOD_RETURN_CODE


def test_scores_service(app_url):
    # @link:https://stackoverflow.com/a/60168019/4000911
    # options = webdriver.ChromeOptions()
    # options.add_argument('--remote-debugging-port=9222')
    # dr = webdriver.Chrome(options=options)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-software-rasterizer")

    # Path to the ChromeDriver
    chrome_driver_path = "/usr/local/bin/chromedriver"

    # Initialize the WebDriver
    dr = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    dr.get(app_url)
    score = dr.find_element(by="id", value="score").text
    return (int(score)) in range(1000)


def main_function():
    app_url = "http://localhost:5000"
    if not test_scores_service(app_url):
        return BAD_RETURN_CODE

    return GOOD_RETURN_CODE


# $> export PYTHONPATH=.
# $> python3 tests/e2e.py
main_function()
