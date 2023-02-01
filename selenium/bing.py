from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

# Make Chrome stay opened
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
# Open Google image search
browser.get('https://www.google.com.hk/imghp?hl=ko&ogbl')
# Find element name q
elem = browser.find_element("name","q")
# Type Hong Kong PolyU
elem.send_keys("Hong Kong PolyU")
# Enter
elem.send_keys(Keys.RETURN)
images = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    imgURL = browser.find_element(By.CSS_SELECTOR, ".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgURL, str(count) + ".jpg")
    count = count + 1