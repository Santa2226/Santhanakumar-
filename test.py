import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#create new instance of chrome webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

#driver = webdriver.Chrome()

#go to this web address
driver.get("https://opensource-demo.orangehrmlive.com/")

#verify the title of the webpage
assert "OrangeHRM" in driver.title

#find the element by id and enter the text
username = driver.find_element_by_name("Username")
username.send_keys("Admin")

#find the element by id and enter the text
password = driver.find_element_by_name("txtPassword")
password.send_keys("admin123")

#find the element by id and click it
login_button = driver.find_element_by_name("login")
login_button.click()

#verify the correct username is displayed on the top right
welcome_message = driver.find_element_by_id("welcome")
assert "Admin" in welcome_message.text

#click on the PIM link on the left side panel
pim_link = driver.find_element_by_id("menu_pim_viewPimModule")
pim_link.click()

#click on the Add Employee link
add_employee_link = driver.find_element_by_id("menu_pim_addEmployee")
add_employee_link.click()

#find the First Name text box and enter the text
first_name = driver.find_element_by_id("firstName")
first_name.send_keys("Test")

#find the Last Name text box and enter the text
last_name = driver.find_element_by_id("lastName")
last_name.send_keys("User")

#find the Save button and click it
save_button = driver.find_element_by_id("btnSave")
save_button.click()

#click on the Admin link on the left side panel
admin_link = driver.find_element_by_id("menu_admin_viewAdminModule")
admin_link.click()

#click on the User Management link
user_management_link = driver.find_element_by_id("menu_admin_UserManagement")
user_management_link.click()

#click on the Users link
users_link = driver.find_element_by_id("menu_admin_viewSystemUsers")
users_link.click()

#click on the Add button
add_button = driver.find_element_by_id("btnAdd")
add_button.click()

#select the user role from the drop down list
user_role_drop_down = driver.find_element_by_id("systemUser_userType")
user_role_drop_down.click()

#find the element by xpath and click it
admin_role = driver.find_element_by_xpath("//*[@id='systemUser_userType']/option[1]")
admin_role.click()

#select the employee name from the drop down list
employee_name_drop_down = driver.find_element_by_id("systemUser_employeeName_empName")
employee_name_drop_down.click()

#find the element by xpath and click it
employee_name = driver.find_element_by_xpath("//*[@id='systemUser_employeeName_empName']/option[2]")
employee_name.click()

#find the element by id and enter the text
user_name = driver.find_element_by_id("systemUser_userName")
user_name.send_keys("TestUser")

#find the element by id and enter the text
status_radio_button = driver.find_element_by_id("systemUser_status")
status_radio_button.click()

#find the element by id and enter the text
password = driver.find_element_by_id("systemUser_password")
password.send_keys("TestUser123")

#find the element by id and enter the text
confirm_password = driver.find_element_by_id("systemUser_confirmPassword")
confirm_password.send_keys("TestUser123")

#find the Save button and click it
save_button = driver.find_element_by_id("btnSave")
save_button.click()

#find the element by id and enter the text
search_user_name = driver.find_element_by_id("searchSystemUser_userName")
search_user_name.send_keys("TestUser")

#find the element by id and click it
search_button = driver.find_element_by_id("searchBtn")
search_button.click()

#verify the user is created
user_name = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr/td[2]")
assert "TestUser" in user_name.text

#click on the logout link
logout_link = driver.find_element_by_id("welcome")
logout_link.click()

#find the element by xpath and click it
logout = driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
logout.click()

#find the element by id and enter the text
username = driver.find_element_by_id("txtUsername")
username.send_keys("TestUser")

#find the element by id and enter the text
password = driver.find_element_by_id("txtPassword")
password.send_keys("TestUser123")

#find the element by id and click it
login_button = driver.find_element_by_id("btnLogin")
login_button.click()

#verify the login is successful
welcome_message = driver.find_element_by_id("welcome")
assert "Test User" in welcome_message.text

#click on the logout link
logout_link = driver.find_element_by_id("welcome")
logout_link.click()

#find the element by xpath and click it
logout = driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
logout.click()

#quit the webdriver
driver.quit()