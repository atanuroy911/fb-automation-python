import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PATH = './chromedriver'

# Handling of Allow Pop Up In Facebook
option = Options()
# option.headless = True
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(options=option, executable_path=PATH)
driver.maximize_window()
driver.get("https://www.facebook.com/")


# Login To The Account
def login(id, password):
    email_box = driver.find_element(By.ID, value="email")
    email_box.send_keys(id)
    password_box = driver.find_element(By.ID, value="pass")
    password_box.send_keys(password)
    driver.find_element(By.NAME, value="login").click()
    pass


# Click on home button to get post section
def click_home():
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li["
                                        "1]/span/div/a").click()
    pass


# Post Content On FaceBook
# def post_content(post):
#     driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div["
#                                         "2]/div/div/div/div[3]/div/div[ "
#                                         "2]/div/div/div/div[1]/div/div[1]/span").click()
#     time.sleep(3)  # A 3 second break in the program so that everythin loads perfectly
#     actions = ActionChains(driver)  # Action Chains
#     actions.send_keys(post)
#     actions.send_keys(Keys.TAB * 10)  # Press TAB 10 Times to reach POST button
#     actions.send_keys(Keys.ENTER)  # Press ENTER to post the content on facebook
#     actions.perform()  # To perfrom all the operations in the action chains
#     pass

# Actions Class
def dropdown_actions():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    pass


# Upload Image
def fb_marketplace_upload_img(img):
    c = driver.find_element(By.XPATH, value="//input[@type='file']")
    c.send_keys(os.path.abspath(img))


# Go to Facebook Marketplace & post
def facebook_marketplace_post(location, img, mak, mod, mile, cost, desc_text):
    driver.get("https://www.facebook.com/marketplace/create/vehicle")
    # actions = ActionChains(driver)
    # actions.send_keys(Keys.TAB * 12)
    # actions.send_keys(Keys.ENTER)
    # actions.send_keys(Keys.ARROW_DOWN)
    # actions.send_keys(Keys.ENTER)
    # actions.perform()

    # Click Vehicle Type
    time.sleep(2)
    driver.find_element(By.XPATH, value="//label[@aria-label='Vehicle type']").click()

    # Click Vehicle Type Option
    dropdown_actions()

    # Upload Image
    fb_marketplace_upload_img(img)

    # Click Location
    loc = driver.find_element(By.XPATH, value="//input[@type='text'][@aria-label='Enter a town or city']")
    loc.click()
    loc.send_keys(location)
    time.sleep(3)  # Wait for results
    # Click 1st search result
    dropdown_actions()
    # Click Year
    driver.find_element(By.XPATH, value="//span[text()='Year']/following::div[1]").click()
    dropdown_actions()

    # Click Make and set Make
    make = driver.find_element(By.XPATH, value="//span[text()='Make']/following::input[1]")
    make.send_keys(mak)

    # Click Model and set Model
    model = driver.find_element(By.XPATH, value="//span[text()='Model']/following::input[1]")
    model.send_keys(mod)

    # Click Mileage and set Mileage
    mileage = driver.find_element(By.XPATH, value="//span[text()='Mileage']/following::input[1]")
    mileage.send_keys(mile)

    # Click Price and set Price
    price = driver.find_element(By.XPATH, value="//span[text()='Price']/following::input[1]")
    price.send_keys(cost)

    # Click Clean Status

    driver.find_element(By.XPATH, value="//input[@name='title_status']").click()

    # Click Vehicle condition Type and set condition
    driver.find_element(By.XPATH, value="//span[text()='Vehicle condition']/following::div[1]").click()
    dropdown_actions()

    # Click Vehicle body Type and set body style
    driver.find_element(By.XPATH, value="//span[text()='Body style']/following::div[1]").click()
    dropdown_actions()

    # Click Vehicle Fuel Type and set Fuel type
    driver.find_element(By.XPATH, value="//span[text()='Fuel type']/following::div[1]").click()
    dropdown_actions()

    # Click Vehicle Transmission Type and set Transmission type
    driver.find_element(By.XPATH, value="//span[text()='Transmission']/following::div[1]").click()
    dropdown_actions()

    # Click Description and set Description
    desc = driver.find_element(By.XPATH, value="//span[text()='Description']/following::textarea[1]")
    desc.send_keys(desc_text)
    pass


def submit_fb_marketplace():
    driver.find_element(By.XPATH, value="//div[@aria-label='Next']/div[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, value="//div[@aria-label='Publish']").click()
    pass

login("rasoco7688@akapple.com", "https://temp-mail.org/en/")
time.sleep(5)
# click_home()
time.sleep(5)
location = "Dhaka"
img = "/Volumes/AIO/PROJECTS/WORK/JOB_DOCS/WIZZARTECH/PROJECTS/0. FB Marketplace AUTOMATION/FB " \
      "AUTOMATION/porsche-911.jpeg "
makeY = "2021"
modelCar = "Porsche 911"
mileCar = "2000"
money = "20000"
description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
              "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and " \
              "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap " \
              "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
              "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
              "software like Aldus PageMaker including versions of Lorem Ipsum. "

facebook_marketplace_post(location, img, makeY, modelCar, mileCar, money, description)
time.sleep(2)
submit_fb_marketplace()
# content = "I am a Cat Posting On Facebook"  ## Demo Content
# post_content(content)
