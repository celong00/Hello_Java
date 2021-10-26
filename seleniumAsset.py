# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:33:58 2021

@author: PREDATOR
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path='C:/Users/PREDATOR/Desktop/chromedriver.exe')
driver.get("http://localhost:9000/shift/adm/login")


# #Login super admin
# email_field = driver.find_element_by_name("email")
# password_field = driver.find_element_by_name("password")

# email_field.send_keys("admin@shiftsoft.org")

# password_field.send_keys("12345678")
# submit_button = driver.find_element_by_name("submitted")
# submit_button.click()
# driver.save_screenshot("screenshot_Asset_Login.png")


# asset_drop = driver.find_element_by_link_text("Assets")
# asset_drop.click()
# time.sleep(1)

#Login User Dummy
email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")

email_field.send_keys("admin@shiftsoft.org")

password_field.send_keys("12345678")
submit_button = driver.find_element_by_name("submitted")
submit_button.click()
driver.save_screenshot("screenshot_ASset_Login_User_Dummy.png")


asset_drop = driver.find_element_by_link_text("Assets")
asset_drop.click()
time.sleep(1)

##Asset categories
category_button = driver.find_element_by_id("Asset Categories")
category_button.click()

# Create
category_add = driver.find_element_by_id("btn-create")
category_add.click()
time.sleep(1)
name_Field = driver.find_element_by_name("name")
name_Field.send_keys("Asset_Category_1")
save_button = driver.find_element_by_id("btn-submit")
save_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()
time.sleep(1)

#Update
time.sleep(1)
update_button = driver.find_elements_by_class_name("btn-update")
update_button[0].click()
time.sleep(1)
name_Field = driver.find_element_by_name("name")
name_Field.clear()
name_Field.send_keys("Asset_Category_1_Update")
save_button = driver.find_element_by_id("btn-submit")
save_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()
time.sleep(1)

# Delete
time.sleep(1)
remove_button = driver.find_elements_by_class_name("btn-delete")
remove_button[0].click()
time.sleep(1)
confirm_remove_button = driver.find_element_by_class_name("btn-submit-delete")
confirm_remove_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()
time.sleep(1)


##Assets
asset_button = driver.find_element_by_id("Assets")
asset_button.click()

# Create
asset_add = driver.find_element_by_id("btn-create")
asset_add.click()
time.sleep(1)
name_Field = driver.find_element_by_name("name")
name_Field.send_keys("Assets_1")
# select = driver.find_elements_by_class_name("chosen")

# select[0].click()
driver.find_element_by_xpath("//select[@name='categoryID']/option[text()='Asset_Category_1']").click()
desc_Field = driver.find_element_by_name("description")
desc_Field.send_keys("Assets_1_Description")
driver.find_element_by_xpath("//select[@name='userId']/option[text()='Super Admin']").click()
save_button = driver.find_element_by_id("btn-submit")
save_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()
time.sleep(1)

# Update
time.sleep(1)
update_button = driver.find_elements_by_class_name("btn-update")
update_button[0].click()
time.sleep(1)
name_Field = driver.find_element_by_name("name")
name_Field.clear()
name_Field.send_keys("Assets_1_Update")
desc_Field = driver.find_element_by_name("description")
desc_Field.clear()
desc_Field.send_keys("Assets_1_Description_Update")
save_button = driver.find_element_by_id("btn-submit")
save_button.click()
close_button = driver.find_elements_by_class_name("close")
close_button[0].click()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.close()

# #Approve
# time.sleep(1)
# update_button = driver.find_elements_by_class_name("btn-read")
# update_button[0].click()
# time.sleep(1)
# save_button = driver.find_elements_by_class_name("btn-approve")
# save_button[0].click()
# close_button = driver.find_elements_by_class_name("close")
# close_button[0].click()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)

# #Disapprove
# time.sleep(1)
# update_button = driver.find_elements_by_class_name("btn-read")
# update_button[0].click()
# time.sleep(1)
# save_button = driver.find_elements_by_class_name("btn-disapprove")
# save_button[0].click()
# close_button = driver.find_elements_by_class_name("close")
# close_button[0].click()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
