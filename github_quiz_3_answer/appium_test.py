from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import time, os, subprocess

from appium.webdriver.webdriver import WebDriver

def pre_test(apkpath='app-debug-1.0.0.apk', devicenm='127.0.0.1:62001'):
    # get activity name and package name with aapt.exe.
    # activity name:
    # cn.ianzhang.android.MainActivity
    # Package name: 
    # cn.ianzhang.android
    p1 = subprocess.Popen(['aapt', 'dump', 'badging', apkpath], 
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
    p1_output, _ = p1.communicate()
    # print(p1_output)
    p2  = subprocess.Popen(['findstr', 'activity'], 
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            encoding='utf-8',)
    p2_output, _ = p2.communicate(input=p1_output)
    activityui = p2_output.split(" ")[1][6:-1]
    print(f"activityui: {activityui}")
    # print(p1_output)
    p3  = subprocess.Popen(['findstr', 'package'], 
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            encoding='utf-8',)
    p3_output, _ = p3.communicate(input=p1_output)
    package = p3_output.split(" ")[1][6:-1]
    print(f"package: {package}")
    # install app
    install_package(package, apkpath)
    #  Json config in Appium UI:
    #     {
    #   "platformName": "Android",
    #   "appium:automationName": "UiAutomator2",
    #   "appium:deviceName": "127.0.0.1:62001",
    #   "appium:app": "app-debug-1.0.0.apk",
    #   "appActivity": "cn.ianzhang.android.MainActivity",
    #   "newCommandTimeout": 3000,
    #   "noReset": true,
    #   "autoGrantPermissions": true
    # }
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': devicenm,
        'app': f'{os.getcwd()}/{apkpath}',
        'appPackage': package,
        'appActivity': activityui,
        'newCommandTimeout': 300,
        'noReset': True,
        'autoGrantPermissions': True}
    
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", 
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    wait = WebDriverWait(driver, 10)
    return driver

def install_package(app, apkpath) -> bool:
    os.system(f"adb push {apkpath} /sdcard/Download | adb uninstall {app} | adb install -r {apkpath}") 
    return True

def tests():
    # initialize driver
    driver = pre_test()
    time.sleep(5)
    # test 1: check all resources on page 1
    ## step 1: check if the first page label is "Hello Ian"
    try:
        lablefirstpage = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/textview_first").text
        assert lablefirstpage == "Hello Ian"
        print("test 1 - step 1:'check Hello Ian label' passed.")
    except Exception as e:
        print(f"test 1 - step 1:'check Hello Ian label' failed: {e}")
    driver.get_screenshot_as_file("screenshots//test1_step1-hello Ian.png")
    ## step 2: check First Page label
    try:
        firstlabel = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView").text
        assert firstlabel == "First Page"
        print("test 1 - step 2:'check First Page label' passed.")
    except Exception as e:
        print(f"test 1 - step 2:'check First Page label' failed: {e}")
    driver.get_screenshot_as_file("screenshots//test1_step2-First Page.png")
    ## setp 3: check more button is clickable and open settings item
    try:
        morebtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "更多选项")
        morebtn.click()
        time.sleep(2)
        title = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/title")
        assert title.text == "Settings"
        # close the settings dialog
        title.click()
        print("test 1 - step 3:'check more button is clickable and open settings item' passed.")
    except Exception as e:
        print(f"test 1 - step 3:'check more button is clickable and open settings item' failed: {e}")
        driver.get_screenshot_as_file("screenshots//test1_step3-more button and Settings.png")
    ## step 4: check mail button and message
    try:
        mailbtn = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/fab")
        mailbtn.click()
        time.sleep(1)
        message = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/snackbar_text").text
        assert message == "This is a demo for Appium Inspector"
        print("test 1 - step 4: 'check mail button and message' passed.")
    except Exception as e:
        print(f"test 1 - step 4: 'check mail button and message'failed: {e}")
    driver.get_screenshot_as_file("screenshots//test1_step4-mail button and message.png")
    ## step 5: check next button and click
    try:
        nextbtn = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/button_first")
        nextbtn.click()
        time.sleep(2)
        secondlabel = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView").text
        assert secondlabel == "Second Page"
        print("test 1 - step 5: 'check next button and click' passed.")
    except Exception as e:
        print(f"test 1 - step 5: 'check next button and click'failed: {e}")
    driver.get_screenshot_as_file("screenshots//test1_step5-check next button and click.png")
    
    # test 2: check resources on page 2
    ## step 1: check back button is clickable and return to first page
    try:
        backbtn = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc=\"转到上一层级\"]")
        backbtn.click()
        time.sleep(2)
        firstlabel = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        assert firstlabel.text == "First Page"
        print("test 2 - step 1:'check back button is clickable and return to first page' passed.")
    except Exception as e:
        print(f"test 2 - step 1:'check back button is clickable and return to first page' failed: {e}")
    driver.get_screenshot_as_file("screenshots//test2_step1-check back button is clickable and return to first page.png")
    
    ## step 2: check if the second page button is clickable
    try:
        # back to second page
        nextbtn = driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/button_first")
        nextbtn.click()
        time.sleep(2)
        driver.find_element(AppiumBy.ID, "cn.ianzhang.android:id/button_second").click()
        time.sleep(2)
        firstlabel = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView").text
        assert firstlabel == "First Page"
        print("test 2 - step 2:'check if the second page button is clickable' passed.")
    except Exception as e:
        print(f"test failed: {e}")
        print("test 2 - step 2:'check if the second page button is clickable' failed.")
    driver.get_screenshot_as_file("screenshots//test2_step2-check if the second page button is clickable.png")  

if __name__ == '__main__':
    tests()
