from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.artstation.com/")

driver.find_element_by_xpath('//*[@id="main-nav"]/ul/li[7]/a/span').click()

username = driver.find_element_by_xpath('//*[@id="user_email"]')
password = driver.find_element_by_xpath('//*[@id="user_password"]')
username.send_keys("jardielsone@gmail.com")
password.send_keys("Psw@2022")
login_attempt = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div[1]/form/div[3]/button')
login_attempt.submit()

driver.find_element_by_xpath('//*[@id="main-menu-nav"]/ul/li[11]/a').click()