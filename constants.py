class Url:
    #  Url's
    url_meet = 'https://meet.google.com/rjv-tajd-syt'
    url_gLogin = 'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier'


class Xpath:
    # XPaths
    email_xpath = "//*[@id='identifierId']"
    password_xpath = "//*[@id='password']/div[1]/div/div[1]/input"
    mic_btn_xpath = "/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div"
    camera_btn_xpath = "/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div"
    joinNow_btn_xpath = "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]"
    askToJoin_btn_xpath = "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]"
    chat_btn_xpath = "//div[@class='pHsCke']/div[@class='Jrb8ue']/div[@class='lvE3se']/div[@class='NzPR9b']/div[@class='uArJ5e UQuaGc kCyAyd kW31ib foXzLb ']"
    textArea_xpath = "//textarea[@class='KHxj8b tL9Q4c']"
    sendBtn_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]"


class Id:
    # Id's
    email_next_id = "identifierNext"
    password_next_id = "passwordNext"


class String:
    # Strings
    exit_msg = "GOODBYE FOLKS...CODED WITH LOVE BY 'XURDE'"
    greet_msg = "Good Morning Sir"


# In seconds
meet_duration = 300.00
