from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password") 
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    def enter_username(self, username):
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    CLAIMS_MENU = (By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span") 
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    
    def click_claims_menu(self):
        claims_menu = self.wait.until(EC.presence_of_element_located(self.CLAIMS_MENU))
        claims_menu.click()
    
    def is_dashboard_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.DASHBOARD_HEADER))
            return True
        except:
            return False

class ClaimsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    # Locators
    EMPLOYEE_CLAIMS_TAB = (By.XPATH, "//a[text()='Employee Claims']")
    ASSIGN_CLAIM_BUTTON = (By.XPATH, "//button[text()=' Assign Claim ']")
    EMPLOYEE_NAME_FIELD = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_OPTION = (By.XPATH, "//div[@role='option']//span[contains(text(), 'Amelia')]")
    EVENT_DROPDOWN = (By.XPATH, "//label[text()='Event']/../following-sibling::div//div[@class='oxd-select-text-input']")
    CURRENCY_DROPDOWN = (By.XPATH, "//label[text()='Currency']/../following-sibling::div//div[@class='oxd-select-text-input']")
    CREATE_BUTTON = (By.XPATH, "//button[text()=' Create ']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']//p[2]")
    
    # Expense locators
    ADD_EXPENSE_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    EXPENSE_TYPE_DROPDOWN = (By.XPATH, "//label[text()='Expense Type']/../following-sibling::div//div[@class='oxd-select-text-input']")
    EXPENSE_DATE_FIELD = (By.XPATH, "//label[text()='Date']/../following-sibling::div//input")
    AMOUNT_FIELD = (By.XPATH, "//label[text()='Amount']/../following-sibling::div//input")
    SUBMIT_BUTTON = (By.CLASS_NAME, "oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
                                
    BACK_BUTTON = (By.XPATH, "//button[text()=' Back ']")
    
    def click_employee_claims(self):
        employee_claims = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_CLAIMS_TAB))
        employee_claims.click()
    
    def click_assign_claim(self):
        assign_claim = self.wait.until(EC.element_to_be_clickable(self.ASSIGN_CLAIM_BUTTON))
        assign_claim.click()
        time.sleep(2)
    
    def select_employee(self, employee_name):
        employee_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_FIELD))
        employee_field.send_keys(employee_name)
        time.sleep(2)
        employee_option = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_OPTION))
        employee_option.click()
    
    def select_event(self, event_name):
        event_dropdown = self.wait.until(EC.element_to_be_clickable(self.EVENT_DROPDOWN))
        event_dropdown.click()
        time.sleep(1)
        event_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{event_name}']")))
        event_option.click()
    
    def select_currency(self, currency):
        currency_dropdown = self.wait.until(EC.element_to_be_clickable(self.CURRENCY_DROPDOWN))
        currency_dropdown.click()
        time.sleep(1)
        currency_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{currency}']")))
        currency_option.click()
    
    def click_create(self):
        create_btn = self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON))
        create_btn.click()
    
    def get_success_message(self):
        try:
            success_msg = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
            return success_msg.text
        except:
            return "No success message found"
    
    def add_expense(self, expense_type, date, amount):
        add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_EXPENSE_BUTTON))
        add_btn.click()
        time.sleep(2)
        
        # Select expense type
        expense_type_dropdown = self.wait.until(EC.element_to_be_clickable(self.EXPENSE_TYPE_DROPDOWN))
        expense_type_dropdown.click()
        time.sleep(1)
        type_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{expense_type}']")))
        type_option.click()
        
        # Enter date
        date_field = self.wait.until(EC.element_to_be_clickable(self.EXPENSE_DATE_FIELD))
        date_field.clear()
        date_field.send_keys(date)
        
        # Enter amount
        amount_field = self.wait.until(EC.element_to_be_clickable(self.AMOUNT_FIELD))
        amount_field.clear()
        amount_field.send_keys(amount)
    
    def click_submit(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_btn.click()
    
    def click_back(self):
        back_btn = self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON))
        back_btn.click()
    
    def is_claim_in_list(self, employee_name):
        try:
            claim_record = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(text(), '{employee_name}')]")))
            return True
        except:
            return False