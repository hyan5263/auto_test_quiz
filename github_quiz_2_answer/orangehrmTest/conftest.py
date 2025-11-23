import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils import ScreenshotManager
from pages import LoginPage, DashboardPage, ClaimsPage

@pytest.fixture(scope="session")
def browser():
    '''
    setup browser driver
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    service = Service(executable_path='drivers//chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def screenshot_manager(browser):
    '''
    screenshot manager for each test function
    '''
    return ScreenshotManager(browser)

@pytest.fixture(scope="function")
def page_objects(browser):
    '''
    page objects
    '''
    return {
        'login_page': LoginPage(browser),
        'dashboard_page': DashboardPage(browser),
        'claims_page': ClaimsPage(browser)}

@pytest.fixture(scope="function")
def test_data():
    """store test data for verification"""
    return {}