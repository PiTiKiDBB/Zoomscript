import pyautogui
import time
import subprocess
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


pyautogui.FAILSAFE = True
'''
#selecting period 
def pick():

pick()
'''
#joining the selected period
prd = "7" #input("Which period would you like to join? ")
pswdInpt = input("Does this meeting require a password? (Y/N): ").upper()

print("Opening page...")
driver = webdriver.Firefox()
driver.get("file:///home/pitikidbb/Desktop/code/temp_zoomhtml/index.html")

if pswdInpt == "Y":
    print("Copying password...")
    copypswd = driver.find_element_by_name(prd + str("pss"))
    copypswd.send_keys(Keys.CONTROL, 'a')
    copypswd.send_keys(Keys.CONTROL, 'c')
elif pswdInpt == "N":
    pass
element = driver.find_element_by_id(prd).click()
time.sleep(1)

print("Joining meeting...")
time.sleep(1)
open2 = pyautogui.locateOnScreen("/home/pitikidbb/Desktop/code/Zoomscript/open2.png")
pyautogui.click(open2)
 

if pswdInpt == "Y":
    print("Pasting in password...")
    pyautogui.hotkey('ctrl', 'v')

print("You are in your meeting!")
'''
if pswd != None:
    pyautogui.typewrite("Password")
else:
    print("Did not find pswd")
'''