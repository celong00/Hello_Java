# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:11:22 2021

@author: PREDATOR
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path='C:/Users/PREDATOR/Desktop/chromedriver.exe')
driver.get("http://localhost:9000/shift/adm/login")


#Login
email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")

email_field.send_keys("admin@shiftsoft.org")

password_field.send_keys("12345678")
submit_button = driver.find_element_by_name("submitted")
submit_button.click()
driver.save_screenshot("screenshot_event_Login.png")

events_button = driver.find_element_by_link_text("Events")
events_button.click()

#Create
events_add = driver.find_element_by_id("btn-create")
events_add.click()

time.sleep(1)
name_Field = driver.find_element_by_id("name")
name_Field.send_keys("Events1_Testing")


select = driver.find_elements_by_class_name("chosen-single")

select[0].click()
select_circle = driver.find_elements_by_class_name("active-result")
select_circle[1].click()

select[1].click()
select_asset = driver.find_elements_by_class_name("active-result")
select_asset[3].click()

# place_Field = driver.find_element_by_id("place")
# place_Field.send_keys("Place1 Testing")

content_Field = driver.find_element_by_id("content")
content_Field.send_keys("Content1 Testing")

startAt_field = driver.find_element_by_name("startAt")
startAt_field.send_keys("05-11-1911")
date_button = driver.find_element_by_link_text("16")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

endAt_field = driver.find_element_by_name("endAt")
endAt_field.click()
date_button = driver.find_element_by_link_text("17")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

remindAt_field = driver.find_element_by_name("remindAt")
remindAt_field.click()
date_button = driver.find_element_by_link_text("15")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

remindAt_field = driver.find_element_by_name("joinMeetingTime")
remindAt_field.click()
date_button = driver.find_element_by_link_text("15")
date_button.click()

driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
save_button = driver.find_element_by_id("btn-check-before-submit")
save_button.click()
time.sleep(2)
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
driver.refresh()
time.sleep(2)

# Update
update_button = driver.find_elements_by_class_name("btn-update")
update_button[0].click()
time.sleep(1)

name_Field = driver.find_element_by_id("name")
name_Field.clear()
name_Field.send_keys("Events1_Testing_Update")

select = driver.find_elements_by_class_name("chosen-single")

select[1].click()
select_asset = driver.find_elements_by_class_name("active-result")
select_asset[1].click()

place_Field = driver.find_element_by_id("place")
place_Field.clear()
place_Field.send_keys("Place1_Testing_Update")

content_Field = driver.find_element_by_id("content")
content_Field.clear()
content_Field.send_keys("Content1_Testing_Update")

startAt_field = driver.find_element_by_name("startAt")
startAt_field.send_keys("05-11-1911")
date_button = driver.find_element_by_link_text("17")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

endAt_field = driver.find_element_by_name("endAt")
endAt_field.click()
date_button = driver.find_element_by_link_text("18")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

remindAt_field = driver.find_element_by_name("remindAt")
remindAt_field.click()
date_button = driver.find_element_by_link_text("16")
date_button.click()
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")

remindAt_field = driver.find_element_by_name("joinMeetingTime")
remindAt_field.click()
date_button = driver.find_element_by_link_text("16")
date_button.click()

driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
driver.execute_script("$(\"button[class='dtp-btn-ok btn btn-flat btn-xs']\").click();")
save_button = driver.find_element_by_id("btn-check-before-submit")
save_button.click()
time.sleep(1)
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()

driver.refresh()
time.sleep(2)

#Delete
time.sleep(1)
delete_button = driver.find_elements_by_class_name("btn-delete")
delete_button[0].click()
time.sleep(1)
confirm_remove_button = driver.find_element_by_class_name("btn-submit-delete")
confirm_remove_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.save_screenshot("screenshot_table_notification_Delete.png")
driver.refresh()
time.sleep(1)



# Add Attd
time.sleep(1)
attd_button = driver.find_elements_by_class_name("btn-attd")
attd_button[3].click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
barcode_Field = driver.find_element_by_id("barcode")
barcode_Field.clear()
barcode_Field.send_keys("shift1")
time.sleep(1)
submit_button = driver.find_element_by_id("submit")
submit_button.click()
time.sleep(1)
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Remove Attd
read_button = driver.find_elements_by_class_name("btn-read")
read_button[3].click()
time.sleep(3)

remove_button = driver.find_element_by_id("btn-remove-attendance")
remove_button.click()

driver.switch_to.alert.accept();
time.sleep(1)
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.close()