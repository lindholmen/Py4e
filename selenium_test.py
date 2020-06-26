from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()

driver.get("http://www.bing.com") #url

data = driver.find_element_by_id("").text

driver.save_screenshot("");

driver.find...send_keys("searched keyword")
driver.find.....click()

driver.page_source() # 不会反扒 .get_cookies()

driver.find...send_keys(Keys.CONTROL,"a")

data = driver.find_elements_by_xpath("//[@class = 'class1 class2 class3']") # // represents root directory. / one directory down
for datapoint in data:
    print(datapoint.text)

# 利用find elelment by link text 找到句柄
ActionChains(driver).move_to_element(ac).click(ac).perform()