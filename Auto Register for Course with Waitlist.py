from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from playsound import playsound

x = 1
while x==1:
    PATH = "/Users/brock/Desktop/Driver thing/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://horizon.mcgill.ca/pban1/twbkwbis.P_WWWLogin")
    time.sleep(4)
    username = driver.find_element_by_id("UserID")
    ## this is a fake, placeholder username. input your own for the code to function
    username.send_keys("XXXXXX")
    time.sleep(0.5)
    password = driver.find_element_by_id("PIN")
    ## this is a fake, placeholder password. input your own for the code to function
    password.send_keys("XXXXXX")
    time.sleep(0.4)
    password.send_keys(Keys.RETURN)
    time.sleep(0.3)
    link1 = driver.find_element_by_link_text("Student")
    link1.click()
    time.sleep(0.3)
    link2 = driver.find_element_by_link_text("Registration Menu")
    link2.click()
    time.sleep(0.3)
    link3 = driver.find_element_by_link_text("Step 2: Search Class Schedule and Add Course Sections")
    link3.click()
    time.sleep(3)
    while True:
        try:
            [i.click() for i in driver.find_elements_by_tag_name("input") if i.get_attribute("value") == "Submit"]
            break
        except:pass
    time.sleep(3)

##selects subject. change value to different course code for a different course (Ex. from "POLI" to "HIST")
    while True:
        try:
            [a.click() for a in driver.find_elements_by_tag_name("option") if a.get_attribute("value") == "POLI"]
            break
        except:pass
    time.sleep(3)
    while True:
        try:
            [b.click() for b in driver.find_elements_by_name("SUB_BTN") if b.get_attribute("value") == "Course Search"]
            break
        except:pass
    time.sleep(3)

## Ignore, just defining the register function
    def register():
        checkmark = driver.find_element_by_id("action_id1")
        checkmark.click()
        time.sleep(3)
        while True:
            try:
                [q.click() for q in driver.find_elements_by_name("ADD_BTN") if q.get_attribute("value") == "Register"]
                break
            except:pass
        time.sleep(3)

## Through the Waitlist
    def waitlist():
        box = driver.find_element_by_xpath("/html/body/div[3]/form/table[4]/tbody/tr[2]/td[2]/select")
        box.click()
        time.sleep(0.1)
        box.send_keys("(")
        box.send_keys(Keys.RETURN)
        time.sleep(1)
        butonnn = driver.find_element_by_xpath("/html/body/div[3]/form/input[19]")
        butonnn.click()
        time.sleep(3)        
        
##Selects specific course. change depending on which course you want
    driver.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[10]/td[3]/form/input[30]").click()
    time.sleep(3)
    num = 0
    for i in driver.find_elements_by_xpath("/html/body/div[3]/form/table/tbody/tr[3]/td"):
        try:
            num = int(i.text)
        except: pass
    print(num)

    if num != 0:
        register()
        waitlist()
        driver.close()
        x=2
        time.sleep(600)
    else:
        driver.close()
        time.sleep(600)







    
    

