# Program to google search 

# Author @vinaykarora
from selenium import webdriver
from config import USERNAME, PASSWORD
import time

users = ['vinaykarora']

# Load the chrome driver
driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')

time.sleep(2)

username_field = driver.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = driver.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = driver.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(5)

for user in users:
    driver.get(f"https://www.instagram.com/{user}/")

    time.sleep(2)

    number_of_posts, followers, following = driver.find_elements_by_css_selector(
        '.g47SY')
    # print('Number of Posts:', number_of_posts.text, 'Followers:',
    #       followers.text, 'Following:', following.text)

    bio = driver.find_element_by_css_selector('.-vDIg')
    # print('Bio:', bio.text, sep='\n')

    with open(f"{user}.txt", "w") as file:
        file.write(
            f"Number of Posts: {number_of_posts.text}\nFollowers: {followers.text}\nFollowing: {following.text}\n\nBio:\n{bio.text}")

    time.sleep(1)