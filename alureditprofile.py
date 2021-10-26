# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:18:36 2021

@author: PREDATOR
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:/Users/PREDATOR/Desktop/chromedriver.exe')
driver.get("http://localhost:9000/shift/adm/login")

email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")

email_field.send_keys("admin@shiftsoft.org")

password_field.send_keys("12345678")
submit_button = driver.find_element_by_name("submitted")
submit_button.click()
driver.save_screenshot("screenshot_edit_Profile_Login.png")

member_drop = driver.find_element_by_link_text("Members")
member_drop.click()

member_button = driver.find_element_by_id("Members")
member_button.click()
driver.save_screenshot("screenshot_edit_Profile_click_member.png")
import time 

# input_button = driver.find_elements_by_class_name("fa-angle-double-right")
# input_button[0].click()
# driver.save_screenshot("screenshot_edit_Profile_click_last_page.png")
# input_button[0].send_keys(Keys.RETURN)

time.sleep(1)
update_button = driver.find_elements_by_class_name("btn-update")
update_button[len(update_button)-2].click()
driver.save_screenshot("screenshot_edit_Profile_click_update.png")
# update_button[0].click()
time.sleep(1)
driver.find_element_by_css_selector("input[type='text'][value='Member Test']").send_keys(" Edit")
time.sleep(1)

driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
driver.execute_script("$(\"input[type='radio'][value='2']\").iCheck('check');")
driver.save_screenshot("screenshot_edit_Profile_choose_gender_and_change_name.png")
tab_account_button = driver.find_element_by_link_text("Account")
tab_account_button.click()
time.sleep(1)
submit_button = driver.find_element_by_id("btn-submit")
submit_button.click()
driver.save_screenshot("screenshot_edit_Profile_Success.png")
time.sleep(1)
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()

time.sleep(1)
update_button = driver.find_elements_by_class_name("btn-update")
update_button[len(update_button)-2].click()
driver.save_screenshot("screenshot_edit_Profile_click_update.png")
# update_button[0].click()
time.sleep(1)
field_name = driver.find_element_by_css_selector("input[type='text'][value='Member Test Edit']")
field_name.clear()
field_name.send_keys("Member Test")
time.sleep(1)

driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
driver.execute_script("$(\"input[type='radio'][value='2']\").iCheck('check');")
tab_account_button = driver.find_element_by_link_text("Account")
tab_account_button.click()
time.sleep(1)
submit_button = driver.find_element_by_id("btn-submit")
submit_button.click()
time.sleep(1)
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.close()





# men_input.click()
