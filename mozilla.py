"""
    Description: Goggle Meet Bot <Spam Your Class ;)>
    Version: 1.0
    Author: Atul Aditya Singh <xurdee>
    Release date: 14 Aug 2020
    Contact: atuladityasingh001@gmail.com

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from constants import Xpath, Id, String, Url
import time
import os


def get_credentials():
    creds = []
    if os.path.isfile("credentials.txt"):
        with open("credentials.txt", "r") as f:
            creds = f.read().split(",")
    else:
        print('No such file exists!')
    return creds


def perform_gLogin():
    # Enter the email
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath.email_xpath))).send_keys(
        username)
    # Click next btn
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ids.email_next_id))).click()
    # Enter the password
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, xpath.password_xpath))).send_keys(password)
    # Click the next btn
    pass_nxt = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, ids.password_next_id)))
    time.sleep(1)
    pass_nxt.click()


def start_spamming():
    start_time = time.time()
    start_time = round(start_time, 2)
    # Add the spam messages to a list
    if os.path.isfile("spammessages.txt"):
        with open("spammessages.txt", "r", encoding="utf8", errors="ignore") as spamfile:
            lines = spamfile.readlines()
    else:
        lines = ["Hmm...something went wrong today...but i will be back later..", "i am BINOD!"]
    j = 0
    end_time = time.time()
    end_time = round(end_time, 2)
    while j < 8:
        print(f"loop {j + 1}")
        print(f"{end_time - start_time} seconds")
        if end_time - start_time < 300.00:  # If running time of script is greater than 60 minutes quit...
            for i in range(len(lines)):
                print(f"quote {i + 1}")
                try:
                    WebDriverWait(driver, 100).until(
                        EC.element_to_be_clickable((By.XPATH, xpath.textArea_xpath))).send_keys(lines[i])
                    WebDriverWait(driver, 100).until(
                        EC.element_to_be_clickable((By.XPATH, xpath.sendBtn_xpath))).click()
                except Exception as e:
                    print(e)
                    # If a dialog box appears dismiss it
                    obj = driver.switch_to.alert()
                    obj.dismiss()
                    continue
            end_time = time.time()
            end_time = round(end_time, 2)
            j += 1
        else:
            # display final message and quit...
            WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, xpath.textArea_xpath))).send_keys(string.exit_msg)
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath.sendBtn_xpath))).click()
            break
    return


def greet_teacher():
    try:
        WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, xpath.textArea_xpath))).send_keys(string.greet_msg)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath.sendBtn_xpath))).click()
    except Exception as ex:
        print(ex)
        pass
    return


#  ----------------------------- GLOBALS ---------------------------- #
# Configure Mozilla Options
options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 1)
options.set_preference("permissions.default.camera", 1)

# Choose driver
driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver.exe', options=options)

# Creating instances
url = Url()
ids = Id()
string = String()
xpath = Xpath()

creds = get_credentials()
username = creds[0]  # Email
password = creds[1]  # Password

# ------------------------------------------------------------------- #

if __name__ == '__main__':
    driver.maximize_window()
    driver.get(url.url_gLogin)
    driver.maximize_window()
    # Login to g-mail
    perform_gLogin()
    time.sleep(3)  # After logging in to gmail wait for a moment...
    # Wait for the meet url to load...
    driver.get(url.url_meet)
    # Turn Off the Mic
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath.mic_btn_xpath))).click()
    # Turn Off the Camera
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath.camera_btn_xpath))).click()
    # Click on 'Ask to join' or 'Join now' btn
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath.joinNow_btn_xpath))).click()
        # driver.find_element_by_xpath(xpath.joinNow_btn_xpath).click()
    except Exception as e:
        print(e)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath.askToJoin_btn_xpath))).click()
        # driver.find_element_by_xpath(xpath.askToJoin_btn_xpath).click()
    # Open ChatBox
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, xpath.chat_btn_xpath))).click()
    # Start Operation
    greet_teacher()
    time.sleep(10)   # Time for which you want to wait before spamming
    start_spamming()
    driver.close()
