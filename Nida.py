from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument ("--start-maximized")
driver = webdriver.Chrome (options = chrome_options)
set_driver (driver)                     # this tells helium to use the selenium webdriver instance

go_to (r"https://www.google.com")


quit()
