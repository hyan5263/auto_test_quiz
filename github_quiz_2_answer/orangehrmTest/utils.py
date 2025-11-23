from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
import os
from datetime import datetime

class WebDriverManager:
    @staticmethod
    def get_driver() -> WebDriver:
        driver_name = WebDriverManager.read_config()
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(executable_path=f'drivers//{driver_name}')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    @staticmethod
    def read_config() -> str:
        with open('drivernm.ini', 'r') as file:
            drivernm = file.read().strip()
        return drivernm

class ScreenshotManager:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.screenshot_dir = "reports/screenshots"
        self.create_screenshot_dir()
        self.screenshots = []
    
    def create_screenshot_dir(self) -> None:
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
    
    def take_screenshot(self, step_name) -> str | None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{step_name}_{timestamp}.png".replace(" ", "_").replace('"', '')
        filepath = os.path.join(self.screenshot_dir, filename)
        try:
            self.driver.save_screenshot(filepath)
            self.screenshots.append({
                'step': step_name,
                'filepath': filepath,
                'timestamp': timestamp})
            return filepath
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None