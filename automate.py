from selenium import webdriver #Web driver implementations
from selenium.webdriver.common.keys import Keys #Provide keys in keyboard

#Create the instance of firefox driver
driver = webdriver.Firefox()

#Navigate to a url
driver.get("http://admin:admin@192.168.1.1/basic/home_wlan.htm")

#Confirm the title
assert "" in driver.title
#Access the element by name
elem = driver.find_element_by_name("PreSharedKey")
#Get access to previous passowrd in my case 49451583
previous = elem.get_attribute('value')
first = int(previous)//1000000
if(first == 99):
    new = str('00')
else:
    new = str(first+1)
password = new + previous[2:]
elem.clear()
driver.switch_to_alert().accept()
elem.send_keys(password)

saveButton = driver.find_element_by_name("SaveBtn")
saveButton.click()

f = open('Generated Password.txt','w')
f.write("Password : "+str(password))
f.close()
driver.close()