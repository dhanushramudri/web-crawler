from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Replace with the path to your WebDriver executable (e.g., chromedriver.exe)
driver_path = 'path/to/chromedriver'

# URL to navigate to
url_to_search = "https://www.geeksforgeeks.org/"

# Create Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={driver_path}")

# Create a new instance of the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

def highlight_and_scroll_to_word(driver, word):
    # Highlight the word using JavaScript
    script = f"var searchReg = new RegExp('{word}', 'ig');\
              document.body.innerHTML = document.body.innerHTML.replace(searchReg, '<span style=\"background-color: yellow;\">$&</span>');"
    driver.execute_script(script)

    # Find the first occurrence of the highlighted word
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{word}')]")

    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

try:
    # Navigate to the URL
    driver.get(url_to_search)

    # Wait for the page to load (adjust the sleep duration if needed)
    time.sleep(5)

    # Print the HTML content
    html_content = driver.page_source
    # print(html_content)

    # Word to search for
    search_word = "Duplicate"

    # Highlight and scroll to the word
    highlight_and_scroll_to_word(driver, search_word)

    # Wait for a few seconds to view the highlighted word
    time.sleep(20)  # Adjust the sleep duration as needed

finally:
    # Comment out or remove the following line to keep the browser open
    driver.quit()
