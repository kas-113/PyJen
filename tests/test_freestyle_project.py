from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FR_PROJECT_NAME = "My Freestyle"
FR_PROJECT_DESCRIPTION = "Freestyle project 1"

def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FR_PROJECT_NAME)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    actual_text = browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text
    assert actual_text == FR_PROJECT_NAME


def test_add_description_when_configure(browser):
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FR_PROJECT_NAME)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "// textarea[ @ name = 'description']").send_keys(FR_PROJECT_DESCRIPTION)
    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    description_field = browser.find_element(By.ID, "description-content").text
    assert description_field == FR_PROJECT_DESCRIPTION


def test_edit_description_when_configure(browser):
    new_project_description = "New description for the product"
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FR_PROJECT_NAME)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "// textarea[ @ name = 'description']").send_keys(FR_PROJECT_DESCRIPTION)
    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    browser.find_element(By.ID, "description-link").click()
    edit_description_field_text = browser.find_element(By.XPATH, "//textarea[@name='description']")
    edit_description_field_text.clear()
    edit_description_field_text.send_keys(new_project_description)
    browser.find_element(By.XPATH, "//button[@name='Submit']").click()

    wait = WebDriverWait(browser, 10)
    description_field_text = wait.until(EC.visibility_of_element_located((By.ID, "description-content"))).text

    assert description_field_text == new_project_description
