from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import time

PASSWORD = "Ahah1212"

times = int(input("How many outlook emails you want to create: "))
print("[+] creating .......")


def create_email():
    basic = "sonacc1wpy"
    for _ in range(4):
        num = random.randint(1, 100)
        basic += str(num)
    return basic


def save_mail(mail):
    with open("saved_mails.txt", "a") as file:
        file.write(f"{mail}@outlook.com\n")
    print("[+] this mail is saved to (saved_mails.txt)")


chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrom_options)

driver.get("https://signup.live.com/?lic=1")
time.sleep(5)

while times != 0:
    times -= 1
    # click on create account button
    create_btn = driver.find_element(By.XPATH, '//*[@id="liveSwitch"]')
    create_btn.click()
    time.sleep(5)

    # input an email

    # check if mail is ok
    # then input password
    while True:
        try:
            MAIL = create_email()
            email_textbox = driver.find_element(By.TAG_NAME, 'input')
            email_textbox.send_keys(MAIL, Keys.ENTER)
            time.sleep(3)
            password_textbox = driver.find_element(By.TAG_NAME, 'input')
            password_textbox.send_keys(PASSWORD, Keys.ENTER)
            time.sleep(3)
            break
        except:
            MAIL = create_email()
            email_textbox = driver.find_element(By.TAG_NAME, 'input')
            email_textbox.send_keys(MAIL, Keys.ENTER)
            time.sleep(3)

    # input first and last name
    name_dt = driver.find_elements(By.TAG_NAME, 'input')
    name_dt[0].send_keys("ahmed", Keys.ENTER)
    name_dt[1].send_keys("gamal", Keys.ENTER)
    time.sleep(3)

    select_day = Select(driver.find_element(By.XPATH, '//*[@id="BirthDay"]'))
    select_day.select_by_visible_text("18")

    select_mon = Select(driver.find_element(By.XPATH, '//*[@id="BirthMonth"]'))
    select_mon.select_by_visible_text("August")

    year = driver.find_element(By.XPATH, '//*[@id="BirthYear"]')
    year.send_keys("2000", Keys.ENTER)
    time.sleep(5)

    # wait to solve Captcha
    wait = WebDriverWait(driver, 1000)
    WebDriverWait(driver, timeout=1000).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="StickyFooter"]/button')))
    next_btn = driver.find_element(By.XPATH, '//*[@id="StickyFooter"]/button')
    time.sleep(5)
    driver.find_element(By.TAG_NAME, 'button').click()

    save_mail(MAIL)
    driver.close()
