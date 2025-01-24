from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument ("--start-maximized")
driver = webdriver.Chrome (options = chrome_options)
set_driver (driver)                     # this tells helium to use the selenium webdriver instance

go_to (r"https://bdc-demo.fcc.gov/")

wait_until(Button("Agree").exists, timeout_secs=20)

click("Agree")
click("Sign in")
write('u.lsmperfte.st@gmail.com', into="Username")
wait_until(Button("Next").exists)
click("next")
write("kAc&a-hux5puq9", into="Password")
click("Sign in")
click("0029429628")
click("Create Submission")

#click(Link("Download"))
# element = driver.find_element(By.CSS_SELECTOR, ".border-0")
# element.click()
#click(Text("Download zipped Provider Summary file"))

#try this code than driver find element
#don't use Selenium codes. Use helium codes
#study it
# sleep(5)
quit()