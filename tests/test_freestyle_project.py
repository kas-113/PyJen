from selenium.webdriver.common.by import By


FR_PROJECT_NAME = "My Freestyle"

def test_create_freestyle_project(browser):
    project_name = "My Freestyle"
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(project_name)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    actual_text = browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text
    assert actual_text == project_name


def test_add_description_when_configure(browser):
    project_description = "Freestyle project 1"
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FR_PROJECT_NAME)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "// textarea[ @ name = 'description']").send_keys(project_description)
    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    description_field = browser.find_element(By.ID, "description-content").text
    assert description_field == project_description


