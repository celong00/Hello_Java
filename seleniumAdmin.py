# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:55:13 2021

@author: PREDATOR
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:/Users/PREDATOR/Desktop/chromedriver.exe')
driver.get("http://localhost:9000/shift/adm/login")


# # Login Testing
# email_field = driver.find_element_by_name("email")
# password_field = driver.find_element_by_name("password")
# print(driver.title)
# email_field.clear()
# 2017-09-142017-09-14

# password_field.send_keys("1234567")
# password_field.send_keys(Keys.RETURN)
# driver.save_screenshot("screenshot_login_false.png")
# print(driver.current_url)
# email_field2 = driver.find_element_by_name("email")
# password_field2 = driver.find_element_by_name("password")
# email_field2.clear()
# email_field2.send_keys("admin@shiftsoft.org")

# password_field2.send_keys("12345678")
# password_field2.send_keys(Keys.RETURN)
# driver.save_screenshot("screenshot_login_true.png")


# Register Testing
button_forgot = driver.find_element_by_link_text("I forgot my password")
button_forgot.click()
driver.save_screenshot("screenshot_navigate_forgot.png")


# making it false on purpose
email_field = driver.find_element_by_name("email")
email_field.send_keys("michaelalexanderrustan@gmail.com")
birthday_field = driver.find_element_by_name("birthday")
birthday_field.send_keys("05-11-1911")
button_cancel = driver.find_element_by_class_name("dtp-btn-cancel")
button_cancel.click()
driver.save_screenshot("screenshot_data_forgot_false.png")
button_submit = driver.find_element_by_class_name("btn-submit-forget")
button_submit.click()
driver.save_screenshot("screenshot_forgot_false_but_success.png")

# True Combination
email_field = driver.find_element_by_name("email")
email_field.clear()
email_field.send_keys("shift1@shiffffffttttttsssss.com")
birthday_field = driver.find_element_by_name("birthday")
birthday_field.send_keys("05-10-2021")
button_cancel = driver.find_element_by_class_name("dtp-btn-cancel")
button_cancel.click()
driver.save_screenshot("screenshot_data_forgot_true.png")
button_submit = driver.find_element_by_class_name("btn-submit-forget")
button_submit.click()

driver.save_screenshot("screenshot_forgot_true.png")


driver.close()