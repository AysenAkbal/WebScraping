from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/aysenakbal/Downloads/chromedriver") 
browser.get("https://www.forbes.com/the-worlds-most-valuable-brands/#77f499a9119c")

browser.maximize_window()
time.sleep(2)
browser.get("https://www.forbes.com/companies/apple/?list=powerful-brands/#12f1091d5355")
browser.set_window_size(600,400)
time.sleep(2)
browser.save_screenshot("/Users/aysenakbal/Desktop/img.png")
time.sleep(2)
browser.quit()
