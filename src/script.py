# Program to google search 

# Author @vinaykarora
from selenium import webdriver
from config import EMAIL, PASSWORD
import time
import pandas

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

# Load the chrome driver
driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.gmail.com')

email_field = driver.find_element_by_css_selector('input[type="email"]')
email_field.send_keys(EMAIL)

next_btn = driver.find_element_by_class_name('VfPpkd-LgbsSe')
next_btn.click()

time.sleep(2)

try_again_btn = driver.find_element_by_class_name('VfPpkd-vQzf8d')
try_again_btn.click()

time.sleep(2)

sign_in_btn = driver.find_element_by_xpath("//a[@data-action='sign in']")
sign_in_btn.click()

time.sleep(2)


password_field = driver.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = driver.find_element_by_class_name('VfPpkd-LgbsSe')
login_btn.click()

for i in excel_data.index:
    print(excel_data.loc[i]['Name'])
    # print(i)

    time.sleep(2)

    compose_btn = driver.find_element_by_css_selector('.T-I.T-I-KE.L3')
    compose_btn.click()

    time.sleep(2)

    to_field = driver.find_element_by_name('to')
    to_field.send_keys(excel_data.loc[i]['Email'])

    subject_field = driver.find_element_by_name('subjectbox')
    subject_field.send_keys('Hiiii')

    body_field = driver.find_element_by_css_selector(
        '.Am.Al.editable.LW-avf.tS-tW')
    body_content = f"""Hii {excel_data.loc[i]['Name']},
How fdsaf,
asdfasd
fasdf
    """
    body_field.send_keys(body_content)

    send_btn = driver.find_element_by_css_selector(
        '.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
    send_btn.click()

    time.sleep(5)