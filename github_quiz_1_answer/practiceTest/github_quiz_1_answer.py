from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time, logging

# set logging
logging.basicConfig(
    filename="github_quiz_1_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

# set and launch browser
def chromesetting():
    '''setting function for chrome browser'''
    # create browser driver object
    browserop = Options()
    service=Service(executable_path='chromedriver.exe')
    # Disable sandbox mode, enhance compatibility
    browserop.add_argument('--no-sandbox')
    # keep browser opening
    browserop.add_experimental_option("detach", True)
    browserop.add_argument("--start-maximized")
    # create and launch Browser
    chromebrowser =  webdriver.Chrome(service=service, options=browserop)
    return chromebrowser

def edgesetting():
    '''setting function for edge browser'''
    browserop = edgeOptions()
    service=edgeService(executable_path='msedgedriver.exe')
    browserop.add_argument('--no-sandbox')
    browserop.add_experimental_option("detach", True)
    browserop.add_argument("--start-maximized")
    edgebrowser =  webdriver.Edge(service=service, options=browserop)
    return edgebrowser

def launcher():
    '''launcher function to launch chrome and edge browser'''
    for i in range(2):
        if i == 0:
            driver = chromesetting()
            print(20*'*' + 'Start tests with Chrome' + 20*'*' )
            logging.info(20*'*' + 'Start tests with Chrome' + 20*'*' )
        else:
            driver = edgesetting()
            print(20*'*' + 'Start tests with Edge' + 20*'*' )
            logging.info(20*'*' + 'Start tests with Edge' + 20*'*' )
        run_test(driver=driver)

def run_test(driver):
    '''run_test function to run test cases'''
    # globally set wait time 
    wait10 = WebDriverWait(driver, 10)
    wait1 = WebDriverWait(driver, 1)
    testlogin_tc1(driver, wait10)
    testlogin_tc2(driver, wait10)
    testlogin_tc3(driver, wait10)
    testException_tc1(driver, wait1)
    testException_tc2(driver, wait10)
    testException_tc3(driver, wait10)
    testException_tc4(driver, wait10)
    testException_tc5(driver, wait10)

def testlogin_tc1(driver, wait):
    '''
    Test case 1: Positive LogIn test
    1. Open page
    2. Type username student into Username field
    3. Type password Password123 into Password field
    4. Push Submit button
    5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
    6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
    7. Verify button Log out is displayed on the new page
    '''
    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testlogin-tc1-01-openWebsite.png")
    print(10*'*' + 'testlogin_tc1 start' + 10*'*' )
    logging.info(10*'*' + 'testlogin_tc1 start' + 10*'*')

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Login Page")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testlogin-tc1-02-openLoginPage.png")
        ## step 2: Type username student into Username field
        username_input = wait.until(ec.visibility_of_element_located((By.ID, "username")))
        username_input.send_keys("student")
        ## step 3: Type password Password123 into Password field
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("Password123")
        ## step 4: Push Submit button
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        ## step 5: Verify new page URL contains 
        ## practicetestautomation.com/logged-in-successfully/
        result = "practicetestautomation.com/logged-in-successfully/" in driver.current_url
        try:
            assert result
            print(f"testlogin case1 - step 5 passed.")
            logging.info(f"testlogin case1 - step 5 passed.")
            driver.save_screenshot("screenshots\\testlogin-tc1-03-loginSuccess.png")
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case1 - step 5 failed: {e}")  
        ## step 6: Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        success_msg = driver.find_element(By.XPATH, "//*[@id=\"loop-container\"]/div/article/div[2]/p[1]/strong")
        result = ("Congratulations" or "successfully logged in") in success_msg.text
        try:
            assert result
            print(f"testlogin case1 - step 6 passed.")
            logging.info(f"testlogin case1 - step 6 passed.")
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case1 - step 6 failed: {e}")  
        ## step 7: Verify button Log out is displayed on the new page
        logout_btn = driver.find_element(By.XPATH, "//*[@id=\"loop-container\"]/div/article/div[2]/div/div/div/a")
        try:
            assert logout_btn.text == "Log out"
            print("testlogin case1 - step 7 passed.")
            logging.info("testlogin case1 - step 7 passed.")
            print(10*'*' + "testlogin case1 passed." + 10*'*')    
            logging.info(10*'*' +"testlogin case1 passed." + 10*'*')
        except AssertionError as e:
            logging.error(f"testlogin case1 step 7 failed: {e}") 
    except Exception as e:
        print(e)
        logging.error(f"testlogin case1 failed: {e}")   
    print(10*'*' + 'testlogin_tc1 end' + 10*'*' )
    logging.info(10*'*' + 'testlogin_tc1 end' + 10*'*' )

def testlogin_tc2(driver, wait):
    '''
    Test case 2: Negative username test
    1. Open page
    2. Type username incorrectUser into Username field
    3. Type password Password123 into Password field
    4. Push Submit button
    5. Verify error message is displayed
    6. Verify error message text is Your username is invalid!
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testlogin-tc2-01-openWebsite.png")
    print(10*'*' + 'testlogin_tc2 start' + 10*'*' )
    logging.info(10*'*' + 'testlogin_tc2 strat' + 10*'*' )

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Login Page")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testlogin-tc2-02-openLoginPage.png")
        ## step 2: Type username incorrectUser into Username field
        username_input = wait.until(ec.visibility_of_element_located((By.ID, "username")))
        username_input.send_keys("incorrectUser")
        ## step 3: Type password Password123 into Password field
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("Password123")
        ## step 4: Push Submit button
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        ## step 5: Verify error message is displayed 
        result = driver.find_element(By.XPATH, "//*[@id=\"error\"]")
        try:
            assert result
            print(f"testlogin case2 - step 5 passed.")
            logging.info(f"testlogin case2 - step 5 passed.")
            driver.save_screenshot("screenshots\\testlogin-tc2-03-invalidUsername.png")
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case2 - step 5 failed: {e}")  
        ## step 6: Verify error message text is Your username is invalid! 
        try:
            assert result.text == 'Your username is invalid!'
            print(f"testlogin case2 - step 6 passed.")
            logging.info(f"testlogin case2 - step 6 passed.")
            print("testlogin case2 passed.") 
            logging.info(10*'*' + "testlogin case2 passed." + 10*'*')
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case2 - step 6 failed: {e}")     
    except Exception as e:
        print(e)
        logging.error(f"testlogin case2 failed: {e}" )   
    print(10*'*' + 'testlogin_tc2 end' + 10*'*' )
    logging.info(10*'*' + 'testlogin_tc2 end' + 10*'*' )

def testlogin_tc3(driver, wait):
    '''
    Test case 3: Negative password test
    1. Open page
    2. Type username student into Username field
    3. Type password incorrectPassword into Password field
    4. Push Submit button
    5. Verify error message is displayed
    6. Verify error message text is Your password is invalid!
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testlogin-tc3-01-openWebsite.png")
    print(10*'*' + 'testlogin_tc3 start' + 10*'*')
    logging.info(10*'*' + 'testlogin_tc3 start' + 10*'*')

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Login Page")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testlogin-tc3-02-openLoginPage.png")
        ## step 2: Type username student into Username field
        username_input = wait.until(ec.visibility_of_element_located((By.ID, "username")))
        username_input.send_keys("student")
        ## step 3: Type password incorrectPassword into Password field
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("incorrectPassword")
        ## step 4: Push Submit button
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        ## step 5: Verify error message is displayed 
        result = driver.find_element(By.XPATH, "//*[@id=\"error\"]")
        try:
            assert result
            print(f"testlogin case3 - step 5 passed.")
            logging.info(f"testlogin case3 - step 5 passed.")
            driver.save_screenshot("screenshots\\testlogin-tc3-03-invalidPassword.png")
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case3 - step 5 failed: {e}")  
        ## step 6: Verify error message text is Your password is invalid! 
        try:
            assert result.text == 'Your password is invalid!'
            print(f"testlogin case3 - step 6 passed.")
            logging.info(f"testlogin case3 - step 6 passed.")
            print(10*'*' + "testlogin case3 passed." + 10*'*' )   
            logging.info(10*'*' + "testlogin case3 passed." + 10*'*' )
        except AssertionError as e:
            print(e)
            logging.error(f"testlogin case3 - step 6 failed: {e}")   
    except Exception as e:
        print(e)
        logging.error(f"testlogin case1 failed: {e}")   
    print(10*'*' + 'testlogin_tc3 end' + 10*'*' )
    logging.info(10*'*' + 'testlogin_tc3 end' + 10*'*' )

def testException_tc1(driver, wait):
    '''
    Test case 1: NoSuchElementException
    1. Open page
    2. Click Add button
    3. Verify Row 2 input field is displayed
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testException-tc1-01-openWebsite.png")
    print(10*'*' + 'testException_tc1 start' + 10*'*' )
    logging.info(10*'*' + 'testException_tc1 start' + 10*'*' )

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Exceptions")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testException-tc1-02-openTestExceptions.png")
        ## step 2: Click Add button
        addbtn = wait.until(ec.visibility_of_element_located((By.ID, "add_btn")))
        addbtn.click()
        driver.save_screenshot("screenshots\\testException-tc1-03-openTestExceptions.png")
        ## step 3: Verify Row 2 input field is displayed
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/div/div[3]/div/input")
        except Exception as e:
            print(e)
            assert "no-such-element-exception" in str(e)
            logging.error(f"Row 2 input field is not displayed. {e}" )
            driver.save_screenshot("screenshots\\testException-tc1-04-openTestExceptions.png")
            print(10*'*' + "testException case1 passed." + 10*'*' )   
            logging.info(10*'*' + f"testException case1 passed." + 10*'*' )   
    except Exception as e:
        print(e)
        logging.error(f"testException case1 failed: {e}")   
    print(10*'*' + 'testException_tc1 end' + 10*'*' )
    logging.info(10*'*' + 'testException_tc1 end' + 10*'*' )

def testException_tc2(driver, wait):
    '''
    Test case 2: ElementNotInteractableException
    1. Open page
    2. Click Add button
    3. Wait for the second row to load
    4. Type text into the second input field
    5. Push Save button using locator By.name(“Save”)
    6. Verify text saved
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testException-tc1-01-openWebsite.png")
    print(10*'*' + 'testlogin_tc2 start' + 10*'*')
    logging.info(10*'*' + 'testlogin_tc2 start' + 10*'*')

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Exceptions")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testException-tc2-02-openTestExceptions.png")
        ## step 2: Click Add button
        addbtn = wait.until(ec.visibility_of_element_located((By.ID, "add_btn")))
        addbtn.click()
        driver.save_screenshot("screenshots\\testException-tc2-03-waitIcon.png")
        ## step 3: Wait for the second row to load
        wait.until(ec.visibility_of_element_located((By.ID, "remove_btn")))
        driver.save_screenshot("screenshots\\testException-tc2-04-newRow.png")
        ## step 4: Type text into the second input field
        text_input = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/section/section/div/div[3]/div/input")))
        text_input.send_keys("test string") 
        driver.save_screenshot("screenshots\\testException-tc2-05-inputText.png")
        ## step 5: Push Save button using locator By.name(“Save”)
        try:
            savebtn = driver.find_element(By.NAME, "Save")
            savebtn.click()
        except Exception as e:
            print(e)
            logging.error(f"{e}")
            try:
                assert "element not interactable" in str(e)
                print(10*'*' + "testException case2 passed." + 10*'*' )
                logging.info(10*'*' + "testException case2 passed." + 10*'*' )   
            except Exception as e:
                print(e)
                logging.info({e})
                print(10*'*' + f"testException case2 failed.{e}" + 10*'*')    
                logging.info(10*'*' + "testException case2 failed." + 10*'*')
            driver.save_screenshot("screenshots\\testException-tc2-06-saveButton.png")
        ## step 6: Verify text saved
        try:
            row2_input = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
            assert row2_input.text == "Row 2 was saved"
        except Exception as e:
            print(e)
            logging.error("Row 2 input field is not displayed.")
    except Exception as e:
        print(e)
        logging.error(f"testException case2 failed: {e}")   
    print(10*'*' + 'testException_tc2 end' + 10*'*' )
    logging.info(10*'*' + 'testException_tc2 end' + 10*'*' )

def testException_tc3(driver, wait):
    '''
    Test case 3: InvalidElementStateException
    1. Open page
    2. Clear input field
    3. Type text into the input field
    4. Verify text changed
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testException-tc3-01-openWebsite.png")
    print(10*'*' + 'testException_tc3 start' + 10*'*')
    logging.info(10*'*' + 'testException_tc3 start' + 10*'*')

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Exceptions")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testException-tc3-02-openTestExceptions.png")
        ## step 2: Clear input field
        textfield = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/section/section/div/div[1]/div/input")))
        try:
            textfield.clear()
        except Exception as e:
            print(e)
            logging.error(f"{e}")
            try:
                assert "invalid element state" in str(e)
                print("10*'*' + testException case3 passed." + 10*'*') 
                logging.info(10*'*' + "testException case3 passed." + 10*'*')  
            except Exception as e:
                print(e)
                logging.info({e})
                print(f"testException case3 - step2 failed.{e}")    
                driver.save_screenshot("screenshots\\testException-tc3-03-clearText.png")
        ## step 3: Type text into the input field
        textfield.send_keys("test string") 
        ## step 4: Type text into the second input field
        try:
            row2_input = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
            assert row2_input.text == "Row 2 was saved"
            print(10*'*' + f"testException case3 - step4 failed." + 10*'*' )  
            logging.error(10*'*' + f"testException case3 - step4 failed." + 10*'*')   
        except Exception as e:
            print(e)
            logging.error("Row 2 input field is not displayed.")
            print(10*'*' + "testException case3 passed." + 10*'*')   
            logging.info(10*'*' + "testException case3 passed." + 10*'*' )  
            driver.save_screenshot("screenshots\\testException-tc3-04-inputText.png")
    except Exception as e:
        print( f"testException case3 failed.{e}" )  
        logging.error(f"testException case3 failed: {e}" )   
    print(10*'*' + 'testException_tc3 end' + 10*'*' )
    logging.info(10*'*' + 'testException_tc3 end' + 10*'*' )

def testException_tc4(driver, wait):
    '''Test case 4: StaleElementReferenceException
    1. Open page
    2. Find the instructions text element
    3. Push add button
    4. Verify instruction text element is no longer displayed
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testException-tc4-01-openWebsite.png")
    print(10*'*' + 'testException_tc4 start' + 10*'*' )
    logging.info(10*'*' + 'testException_tc4 start' + 10*'*' )

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Exceptions")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testException-tc4-02-openTestExceptions.png")
        ## step 2: Find the instructions text element
        instruction = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"instructions\"]")))

        ## step 3: Push add button
        addbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"add_btn\"]")))
        addbtn.click()
        time.sleep(8)
        driver.save_screenshot("screenshots\\testException-tc4-03-clickAddbtn.png")
        ## step 4: Verify instruction text element is no longer displayed
        try:
            assert "stale element reference" in instruction.text
            print(10*'*' + "testException case4 failed." + 10*'*' ) 
            logging.info(10*'*' + "testException case4 failed." + 10*'*' ) 
        except Exception as e:
            print(e)
            logging.error(f"The instruction is not displayed.{e}")
            print(10*'*' + "testException case4 passed." + 10*'*' )  
            logging.info(10*'*' + "testException case4 passed." + 10*'*' )  
            driver.save_screenshot("screenshots\\testException-tc4-04-noInstruction.png")
    except Exception as e:
        print(e)
        logging.error(f"testException case4 failed: {e}")  
    print(10*'*' + 'testException_tc4 end' + 10*'*' )
    logging.info(10*'*' + 'testException_tc4 end' + 10*'*' )

def testException_tc5(driver, wait):
    '''Test case 5: TimeoutException
    1. Open page
    2. Click Add button
    3. Wait for 3 seconds for the second input field to be displayed
    4. Verify second input field is displayed
    '''

    # open website
    driver.get("https://practicetestautomation.com/practice/")
    print("open website successfully!")
    driver.save_screenshot("screenshots\\testException-tc5-01-openWebsite.png")
    print(10*'*' + 'testException_tc5 start' + 10*'*' )
    logging.info(10*'*' + 'testException_tc5 start' + 10*'*' )

    try:
        ## step 1: Open page
        login_page_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Test Exceptions")))
        login_page_link.click()
        time.sleep(2)
        driver.save_screenshot("screenshots\\testException-tc5-02-openTestExceptions.png")
        ## step 2: Click Add button
        addbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"add_btn\"]")))
        addbtn.click()
        driver.save_screenshot("screenshots\\testException-tc5-03-clickAddRow.png")
        ## step 3: Wait for 3 seconds for the second input field to be displayed
        time.sleep(3)
        ## step 4: Verify second input field is displayed
        try:
            driver.find_element(By.XPATH, "//*[@id=\"row2\"]/input")
            print(10*'*' + "testException case5 failed." + 10*'*') 
        except Exception as e:
            print(e)
            logging.error(f"Row 2 is not displayed.{e}")
            print(10*'*' + "testException case5 passed." + 10*'*' ) 
            logging.info(10*'*' + "testException case5 passed." + 10*'*' )  
            driver.save_screenshot("screenshots\\testException-tc5-04-row2NotExist.png")
    except Exception as e:
        print(e)
        logging.error(f"testException case5 failed: {e}")   
    print(10*'*' + 'testException_tc5 end' + 10*'*' )
    logging.info(10*'*' + 'testException_tc5 end' + 10*'*' )

if __name__ == "__main__":
    launcher()