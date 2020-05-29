from selenium import webdriver #Web driver implementations
from selenium.webdriver.common.keys import Keys #Provide keys in keyboard
import random #To generate random number
from datetime import date
today = str(date.today()) #Get todays date
import ctypes #For popup window

previousDate = ""
#Make sure the file exists
try:
    f = open('date','r')
    previousDate = f.read()
    f.close()
except Exception:
    pass

#If it is the same date do not perform any operation
if previousDate == today:
    #Notify that password has already been generated
    ctypes.windll.user32.MessageBoxW(0,"Password already generated today!","Password Generator",0)
    pass
else:
    #Create the instance of firefox driver
    #You can call firefox or any other driver you have installed
    driver = webdriver.Firefox()

    #username
    username = "admin"

    #password
    adslPassword = "admin"
    #Navigate to a url
    driver.get("http://"+username+":"+adslPassword+"@192.168.1.1/basic/home_wlan.htm")

    #Confirm the title
    assert "" in driver.title #You can comment this out or change it to your title of the adsl

    #Access the element by name
    elem = driver.find_element_by_name("PreSharedKey")
    password = random.randint(100000000,999999999) #Generate new 9 digit random password
    #Send the password value to the input element
    elem.send_keys(password)

    #Access the save button
    saveButton = driver.find_element_by_name("SaveBtn")

    #Perform a click action
    saveButton.click()

    #Create or edit a file named 'Generated Password.txt'
    f = open('Generated Password.txt','w')
    #Write the new password to it
    f.write("Password : "+str(password))
    #Close the file
    f.close()
    #Popup to show todays password
    ctypes.windll.user32.MessageBoxW(0,"Todays password is :"+password,"Password Generator",1)
    # #Create or edit a file named 'date'
    f = open('date','w')
    #Write todays date to it
    f.write(str(today))
    #Close the file
    f.close()
    #Close the driver
    driver.close()