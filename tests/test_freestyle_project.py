from selenium.webdriver.common.by import By


def test_create_freestyle_project(browser):
    project_name = "My Freestyle"
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(project_name)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Freestyle project')]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    actual_text = browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text
    assert actual_text == project_name


