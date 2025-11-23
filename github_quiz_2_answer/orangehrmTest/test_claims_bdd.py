import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import time

# load feature file
scenarios('features/assign_claims.feature')

# define steps
@given('I am on the OrangeHRM login page')
def i_am_on_login_page(browser, screenshot_manager):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    screenshot_manager.take_screenshot("login_page")

@when('I login with valid credentials')
def login_with_valid_credentials(screenshot_manager, page_objects):
    page_objects['login_page'].enter_username("Admin")
    page_objects['login_page'].enter_password("admin123")
    page_objects['login_page'].click_login()
    time.sleep(3)
    screenshot_manager.take_screenshot("after_login")

@then('I should be redirected to the dashboard')
def verify_dashboard_loaded(screenshot_manager, page_objects):
    assert page_objects['dashboard_page'].is_dashboard_loaded()
    time.sleep(2)
    screenshot_manager.take_screenshot("dashboard")

@given('I navigate to the Claims section')
def navigate_to_claims(browser, screenshot_manager, page_objects, test_data):
    page_objects['dashboard_page'].click_claims_menu()
    time.sleep(2)
    screenshot_manager.take_screenshot("claims_section")

@when('I click on Employee Claims')
def click_employee_claims(browser, screenshot_manager, page_objects, test_data):
    page_objects['claims_page'].click_employee_claims()
    time.sleep(2)
    screenshot_manager.take_screenshot("employee_claims")

@when(parsers.parse('I add a new Assign Claim with employee "{employee_name}", event "{event}", and currency "{currency}"'))
def add_assign_claim(browser, screenshot_manager, page_objects, test_data, employee_name, event, currency):
    page_objects['claims_page'].click_assign_claim()
    page_objects['claims_page'].select_employee(employee_name)
    page_objects['claims_page'].select_event(event)
    page_objects['claims_page'].select_currency(currency)
    
    # store claim data in test_data for verification in later steps
    test_data['claim'] = {
        'employee_name': employee_name,
        'event': event,
        'currency': currency
    }
    time.sleep(2)
    screenshot_manager.take_screenshot("before_create_claim")
    page_objects['claims_page'].click_create()

@then(parsers.parse('I should see success message "{message}"'))
def verify_success_message(browser, screenshot_manager, page_objects, test_data, message):
    actual_message = page_objects['claims_page'].get_success_message()
    assert message in actual_message, f"Expected '{message}' but got '{actual_message}'"
    time.sleep(2)
    screenshot_manager.take_screenshot("success_message")

@then('I should be redirected to Assign Claim details page')
def verify_claim_details_page(browser, screenshot_manager, test_data):
    time.sleep(2)
    screenshot_manager.take_screenshot("claim_details_page")

@then('the claim details should match the entered data')
def verify_claim_details(browser, screenshot_manager, test_data):
    # get claim data from test_data
    claim_data = test_data.get('claim', {})
    time.sleep(2)
    screenshot_manager.take_screenshot("claim_data_verification")
    print(f"Should verify claim data: {claim_data}")

@when(parsers.parse('I add an expense with type "{expense_type}", date "{date}", and amount "{amount}"'))
def add_expense(browser, screenshot_manager, page_objects, test_data, expense_type, date, amount):
    page_objects['claims_page'].add_expense(expense_type, date, amount)
    # store expense data in test_data for verification in later steps
    test_data['expense'] = {
        'expense_type': expense_type,
        'date': date,
        'amount': amount
    }
    time.sleep(2)
    screenshot_manager.take_screenshot("before_submit_expense")
    page_objects['claims_page'].click_submit()

@then(parsers.parse('I should see success message "{message}" for expense'))
def verify_expense_success_message(browser, screenshot_manager, page_objects, test_data, message):
    actual_message = page_objects['claims_page'].get_success_message()
    assert message in actual_message, f"Expected '{message}' but got '{actual_message}'"
    time.sleep(2)
    screenshot_manager.take_screenshot("expense_success_message")

@then('the expense details should match the entered data')
def verify_expense_details(browser, screenshot_manager, test_data):
    # get expense data from test_data for comparison with screenshot
    expense_data = test_data.get('expense', {})
    time.sleep(2)
    screenshot_manager.take_screenshot("expense_data_verification")
    print(f"Should verify expense data: {expense_data}")

@when('I click the Back button')
def click_back_button(browser, screenshot_manager, page_objects, test_data):
    page_objects['claims_page'].click_back()
    time.sleep(2)
    screenshot_manager.take_screenshot("after_back_button")

@then('I should see the newly created claim in the records list')
def verify_claim_in_list(browser, screenshot_manager, page_objects, test_data):
    # get claim data from test_data for verification
    claim_data = test_data.get('claim', {})
    employee_name = claim_data.get('employee_name', '')
    assert page_objects['claims_page'].is_claim_in_list(employee_name), \
        f"Claim for {employee_name} not found in records list"
    time.sleep(2)
    screenshot_manager.take_screenshot("claim_in_records_list")