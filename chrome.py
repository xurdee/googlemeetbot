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
import time
import os


# Get gmail login credentials
def getCreds():
    creds = []
    if os.path.isfile("credentials.txt"):
        with open("credentials.txt", "r") as f:
            creds = f.read().split(",")
    else:
        print('No such file exists!')
    return creds


#  Url's
url_meet = 'https://meet.google.com/bin-bwts-qis'
url_gLogin = 'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier'

# Configure Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1
  })

# Choose driver
driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver.exe',options=options)

if __name__ == '__main__':
    creds = getCreds()
    username = creds[0]  # Email
    password = creds[1]  # Password

    driver.maximize_window()
    driver.get(url_gLogin)
    driver.maximize_window()

    # Enter the email
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']"))).send_keys(
        username)
    # Click next btn
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()
    # Enter the password
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(password)
    # Click the next btn
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()

    time.sleep(3)  # After logging in to gmail wait for a moment...

    # Wait for the meet url to load...
    driver.get(url_meet)
    time.sleep(15)

    # Turn Off the Mic
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                 "/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div"))).click()
    # Turn Off the Camera
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                 "/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div"))).click()

    # Click on 'Ask to join' or 'Join now' btn
    try:
        driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
    except Exception as e:
        print(e)
        driver.find_element_by_xpath(
            "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()

    time.sleep(15)  # Time for which you want to wait before spamming

    # When Playing evil
    chatBtn = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "//div[@class='pHsCke']/div[@class='Jrb8ue']/div[@class='lvE3se']/div[@class='NzPR9b']/div[@class='uArJ5e UQuaGc kCyAyd kW31ib foXzLb ']"))).click()
    start_time = time.time()
    start_time = round(start_time, 2)

    # textArea = driver.find_element_by_xpath("//textarea[@class='KHxj8b tL9Q4c']")
    # sendButton = driver.find_element_by_xpath(
    #     "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]")

    # Add the spam messages to a list
    if os.path.isfile("spammessages.txt"):
        with open("spammessages.txt", "r", encoding="utf8", errors="ignore") as spamfile:
            lines = spamfile.readlines()
    else:
        lines = ["Hmm...something went wrong today...but i will be back later..", "i am BINOD!"]

    j = 0
    end_time = time.time()
    end_time = round(end_time, 2)
    while j < 5:
        print(f"loop {j+1}")
        print(f"{end_time-start_time} seconds")
        if end_time-start_time < 300.00:   # If running time of script is greater than 60 minutes quit...
            for i in range(len(lines)):
                print(f"quote {i+1}")
                try:
                    textArea = WebDriverWait(driver, 100).until(
                        EC.element_to_be_clickable((By.XPATH, "//textarea[@class='KHxj8b tL9Q4c']")))
                    textArea.send_keys(lines[i])
                    sendButton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]")))
                    sendButton.click()
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
            textArea = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@class='KHxj8b tL9Q4c']")))
            # display final message and quit...
            textArea.send_keys(" GOODBYE FOLKS...CODED WITH LOVE BY 'XURDE'")

            sendButton = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                                      "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]")))
            sendButton.click()
            break

    driver.close()