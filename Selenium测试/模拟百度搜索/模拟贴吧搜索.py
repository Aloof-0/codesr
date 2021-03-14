from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"https://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("贴吧")

time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_xpath(r'''//*[@id="1"]/h3/a[1]''').click()
time.sleep(3)
print(driver.title)
time.sleep(3)
driver.quit()
