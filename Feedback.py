from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


croptions = webdriver.ChromeOptions()

croptions.add_argument("--incognito")





def find_sender(driver, path, text):
    driver.find_element(By.CSS_SELECTOR, path).send_keys(text)


try:
    driver = webdriver.Chrome(options=croptions)
    driver.get("123123123")
    driver.implicitly_wait(5)
    # main project
    element = driver.find_element(
        By.CSS_SELECTOR,
        "#request_form > div.request-fields-wrapper > div.request-field-content > div",
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    find_sender(driver, "#request_name", "ssss12")
    find_sender(driver, "#request_phone", "9999999999")
    find_sender(driver, "#request_email", "12344@gfgf.fg")
    find_sender(driver, "#request_company", "test1")
    find_sender(driver, "#request_about", "test1")
    driver.find_element(By.CSS_SELECTOR, "#request_agree_to_privacy_policy").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "#request_form > div.request-fields-wrapper > div.request-field-content > div > div:nth-child(2) > div.select.budget-select > div.select-current.placeholder",
    ).click()

    driver.find_element(
        By.CSS_SELECTOR,
        "#request_form > div.request-fields-wrapper > div.request-field-content > div > div:nth-child(2) > div.select.budget-select.active > div.select-list > li:nth-child(3) > label",
    ).click()
    time.sleep(1)
    driver.find_element(
        By.CSS_SELECTOR,
        "#request_form > div.request-fields-wrapper > div.request-submit-group > div.submit-container > div.submit > input",  ####добавить прогверку на нажатость кнопки
    ).click()

finally:
    time.sleep(10)
    driver.quit()

    # discussion project
    # element = driver.find_element(
    # By.CSS_SELECTOR,
    # "#request_form > div.request-fields-wrapper > div.request-field-content > div",
    # )
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # find_sender(driver, "#request_name", "ssss12")
    # find_sender(driver, "#request_phone", "9999999999")
    # find_sender(driver, "#request_email", "12344@gfgf.fg")
    # find_sender(driver, "#request_company", "test1")
    # find_sender(driver, "#request_about", "test1")
    # driver.find_element(By.CSS_SELECTOR, "#request_agree_to_privacy_policy").click()
