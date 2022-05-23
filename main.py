import os

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

os.environ['PATH'] += r'C:/selenium'

driver = webdriver.Chrome()

base_url = 'https://studybay.app/home/'

driver.get(base_url)

login_email = driver.find_element(By.NAME, 'email')
login_email.send_keys('ogachdniel@yahoo.com')

login_password = driver.find_element(By.NAME, 'password')
login_password.send_keys('Ph.D@2021')

driver.implicitly_wait(5)
login_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/form/button')
login_btn.click()

driver.implicitly_wait(5)
project_search = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/div[1]/a[1]')
project_search.click()

driver.implicitly_wait(3)
more_btn = driver.find_elements(By.CLASS_NAME, 'iIDguA')

for btn in more_btn:
    btn.click()
    driver.implicitly_wait(3)

# place_bid = driver.find_elements(By.CLASS_NAME, 'JkCDS')
# for bid in place_bid:
#     # ActionChains(driver).key_down(Keys.CONTROL).click(bid).key_up(Keys.CONTROL)

project_container = driver.find_element(By.CLASS_NAME, 'styled__OrderListWrapper-sc-1qmwpw4-0')

bid_link_url = project_container.find_elements(By.CLASS_NAME, 'orderA-converted__name')

parent_window = driver.current_window_handle

for url in bid_link_url:
    url.send_keys(Keys.CONTROL, Keys.ENTER)

child_windows = driver.window_handles
print(child_windows)
for child in child_windows:
    if child != parent_window:
        driver.switch_to.window(child)
        try:
            lowest_price = driver.find_element(By.CLASS_NAME, 'fnBQUJ')
            value = lowest_price.text
            print(value)
            price_input = driver.find_element(By.XPATH,
                                              '/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div['
                                              '1]/div[ '
                                              '2]/div/div/div/div[1]/input')
            driver.implicitly_wait(2)
            price_input.send_keys(value)
            submit_bid = driver.find_element(By.XPATH,
                                             '/html/body/div[10]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/button['
                                             '1]/span')
            submit_bid.click()
            driver.implicitly_wait(20)
        except:
            continue

