from selenium import webdriver
import time
driver = webdriver.Chrome()  # "./chromedriver.exe"

driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("大宝贝")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.save_screenshot("./python.png")
time.sleep(3)
driver.quit()
