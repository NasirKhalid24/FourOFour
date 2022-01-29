from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time


# Initializing stuff

driver = webdriver.Chrome('/Users/zafirkhalid/Desktop/ConUHacks/chromedriver')
driver.set_window_position(0, 0)
driver.set_window_size(375, 900)


driver.get("http://www.instagram.com")

time.sleep(1)

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("conutestaccount")
password.clear()
password.send_keys("123Qweasdzxc!")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


time.sleep(1.5)


elements = driver.find_elements_by_xpath("//article[@class='_8Rm4L bLWKA M9sTE _1gNme h0YNM  SgTZ1    ']")


def get_screenshots(elements):
    for i,elem in enumerate(elements):
        driver.execute_script("return arguments[0].scrollIntoView(false);", elem)
        driver.save_screenshot("image" + str(i) + ".png")

def like_image(num):
    img_to_like = elements[num]
    button_to_press = img_to_like.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[3]/div/article["+str(num+1)+"]/div/div[3]/div/div/section[1]/span[1]/button")
    driver.execute_script("arguments[0].click();", button_to_press)