from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

# frontend_testing.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def frontend_test(web_interface_url, user_id):
    global driver
    try:
        driver = webdriver.Chrome()

        # Navigate to the web interface URL using the existing user ID
        driver.get(f"{web_interface_url}/users/get_user_data/{user_id}")

        # Wait for the user name element to be present
        user_name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user")))

        user_name = user_name_element.text
        print(f"User Name: {user_name}")

    finally:
        # Close the WebDriver session
        driver.quit()
    web_interface_url = "http://127.0.0.1:5001"
    existing_user_id = 1
    frontend_test(web_interface_url, existing_user_id)

