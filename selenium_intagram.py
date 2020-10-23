from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("/Users/aysenakbal/Downloads/chromedriver")
driver.get("https://www.instagram.com/?hl=tr")

time.sleep(5)

user_name = driver.find_element_by_name("username")
user_pass = driver.find_element_by_name("password")


user_name.send_keys("aysenakbal")
user_pass.send_keys("enter_your_password")

time.sleep(2)

login_button = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
login_button.click()
time.sleep(5)

nosavedata = driver.find_element_by_xpath("//div//button[@class= 'sqdOP yWX7d    y3zKF     ']")
nosavedata.click()
time.sleep(3)

close_notification = driver.find_element_by_xpath("//div//button[@class='aOOlW   HoLwm ']")
close_notification.click()
time.sleep(4)

profil_page = driver.find_element_by_xpath("//div//span[@class='_2dbep qNELH']")
profil_page.click()

time.sleep(2)

click_profile = driver.find_element_by_xpath("//a//div[@class='                    Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                  La5L3 ZUqME']")
click_profile.click()

time.sleep(3)

followers_page = driver.find_element_by_xpath("//ul//li[2][@class ='Y8-fY ']")
followers_page.click()
time.sleep(2)


#find all li elements in list
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")

#SCROLL ICIN DAHA MANTIKLI BIR YOL BUL!!!! 

scroll = 0
while scroll < 100: 
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(3)
    scroll += 1

fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li//div//div[@class='enpQJ']//div[@class='wFPL8 ']")
followerList = []

for follower in fList:
    followerList.append(follower.text)

with open("instagram_follower.txt", "w",encoding="UTF-8") as file:
    for f in followerList:
        file.write(f + "\n" )
time.sleep(5)






