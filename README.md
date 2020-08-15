# googlemeetbot 🤖
A Google Meet Bot to attend your online classes instead of you.
PS: You also have the option to spam the chatBox (But of course use it at your own risk. Do not blame me for the consequences that follow).

## REQUIREMENTS
      $ pip3 install selenium
      $ pip3 install pause
      
  I encourage you to work on a virtual enviornment like anaconda
  
### My Test Cases

* Firstly I worked with the selenium chrome-driver and used chrome as the interface =  WORKS 
* Secondly I tried it  using headless mode enabled in chrome = BUG 
* I then tried using geckodriver and Firefox = WORKS
* I then tried headless mode in Firefox = WORKS LIKE CHARM

## Advantages of headless drivers?
   
The program runs in background until you have a good internet connection and power . It never requires mozilla tab to be opened . I really worked on chrome-headless but some bugs reported while running so i switched to the mozilla-headless which works like charm.
   
### CODE
  * chrome.py
  * mozilla.py
  * constants.py
 
# Initial Steps

  * In the credentials.txt file replace the <username> and <password> with your gmailid and password.
  
  * In the constants.py replace the url meet with the meeting id.
  
# Working Of chrome.py
  
  * Download chromedriver.exe from https://chromedriver.chromium.org/downloads (You can choose the chromedriver that suits the version of your chrome browser. To check your 
    chrome version go to Settings ---> About Chrome  by clicking the three dots in the top right.
  
  * Once chromedriver has been downloaded it will be in form of a zip file , extract the content of the zip file to the project directory. (In the same folder where your chrome.py lies).
  * You can uncomment the pause.until in the chrome.py ie you can set the time and execute when to start the program
  
## Note : The headless chrome functionality is buggy and is not working. So i strongly recommend you use Mozilla browser for testing the script.
 
# Working Of mozilla.py 

  * Download geckodriver from https://github.com/mozilla/geckodriver/releases ( Choose the one that suits your OS).
  
  * Extract and place the geckodriver executable in the project directory. (In the same folder where your mozilla.py lies).
 
## Note: 
 * The headless option makes the program to run in background. Even if the program terminates we will be still be the particpants in the meeting.
 * The permission parameters are little different than in chrome-driver.
  
# How To Run The Program Effectively?
  
  * If you deploy it on cloud then the real fun begins. You no longer have to bother about the internet ,time and other stuff.
  
  * If more than one meeting id or classes just use the sys arguments or argparse and pass the id as parameters 😀 Cool isn't it?. 
  
  * Here is a link to help you deploy a headless chrome in goole cloud platform that i found on internet : 
  
  https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp
  
  * If you search for mozilla deploy you can find it too..
  
  * You can deploy the script on heroku or pythonanywhere too
  
 # How To Fire The Script?
      
      For chrome browser : 
      
     # python3 chrome.py 
     
      For mozilla headless. If you want to see mozilla opening just uncomment the headless option in the Firefox Options
      
     # python3 mozilla.py
     
 ## Note : The script will run for about an hour once fired up. You can set the running time according to the duration of your class. (Just go to constants.py and change the value of the variable 'running_time'). 
    
### HAVE A NICE DAY  ☕
