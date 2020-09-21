import pytest
import time
from selenium import webdriver


@pytest.fixture()
def environment_setup():
    global browser
    browser = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    browser.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(15)
    browser.maximize_window()
    yield
    browser.close()

def test_fail(environment_setup):
    uname = browser.find_element_by_name("txtUsername")
    uname.send_keys("Admin")
    pname = browser.find_element_by_name("txtPassword")
    pname.send_keys("admin123")
    Submitbutton = browser.find_element_by_name("Submit")
    Submitbutton.click()

def test_pass(environment_setup):
    uname = browser.find_element_by_name("txtUsername")
    uname.send_keys("Admin")
    forgot = browser.find_element_by_link_text("Forgot your password?")
    forgot.click()
