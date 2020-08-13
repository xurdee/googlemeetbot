from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import pause
from pynput.keyboard import Controller
#######YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)

def getCreds():
    creds = []
    if(os.path.isfile("credentials.txt")):
        with open("credentials.txt", "r") as f:
            creds = f.read().split(",")
    else:
        print('No such file exists!')
    return creds

creds = getCreds()
usernameStr = creds[0]
passwordStr = creds[1]
url_meet = 'https://meet.google.com/sfx-jvvz-xok'
options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)
browser = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver.exe',options=options)
browser.set_window_size(800, 600)
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)
keyboard = Controller()
password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
time.sleep(3)
browser.get(url_meet)
time.sleep(15)
try:
    browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
except Exception as e:
    print(e)
    browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
time.sleep(15)  # Time for which you want to wait before spamming

chatEveryoneButton = browser.find_element_by_xpath("//div[@class='pHsCke']/div[@class='Jrb8ue']/div[@class='lvE3se']/div[@class='NzPR9b']/div[@class='uArJ5e UQuaGc kCyAyd kW31ib foXzLb ']")
chatEveryoneButton.click()
textArea = browser.find_element_by_xpath("//textarea[@class='KHxj8b tL9Q4c']")
sendButton = browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]")
if(os.path.isfile("spammessages.txt")):
    with open("spammessages.txt", "r",encoding="utf8",errors="ignore") as spamfile:
        lines = spamfile.readlines()
else:
    lines = ["Hmm...something went wrong today...but i will be back later..","i am BINOD!"]

j=0
while(j<10):
    for i in range(len(lines)):
        textArea.send_keys(lines[i])
        sendButton.click()
        time.sleep(1)
    j+=1

pause