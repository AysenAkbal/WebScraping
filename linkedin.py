from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/aysenakbal/Downloads/chromedriver")
browser.get("https://www.linkedin.com/home")

browser.fullscreen_window()
time.sleep(2)

#oturum ac butonuna bas
login = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(2)

#enter email address and password
email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("aysennakbal@gmail.com")
password.send_keys("enter_your_password")

login_button = browser.find_element_by_css_selector("#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button")
login_button.click()
time.sleep(2)

search_button = browser.find_element_by_xpath("//*[@id='ember16']/input")
search_button.send_keys("#python")

#after write #python, click enter
search_button.send_keys(Keys.RETURN)
time.sleep(5)

#open contacts page
contacts = browser.find_element_by_xpath("//*[@id='ember23']")
contacts.click()
time.sleep(2)

contacts_page = browser.find_element_by_class_name("mn-community-summary__entity-info")
contacts_page.click()
time.sleep(3)

#scroll
for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

followers = browser.find_elements_by_class_name("mn-connection-card__details")
followerList=[]

for follower in followers:
    followerList.append(follower.text)
with open("followers.txt","w", encoding="UTF-8") as file:
    for follower in followerList:
        file.write(follower + "/n")
time.sleep(5)

browser.quit()