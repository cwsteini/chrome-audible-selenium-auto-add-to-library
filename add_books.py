from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException

# --- Connect to your existing Chrome session ---
opts = Options()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=opts)
print("✅ Connected to existing Chrome window!")

time.sleep(5)  # wait for page to load

while True:
    buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Add to Library')]")
    
    if not buttons:
        break  # done clicking all buttons
    
    for button in buttons:
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(0.4)
            button.click()
            print("✅ Added a book")
            time.sleep(0.8)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            # If element is stale or blocked, skip and continue
            continue

print("🎉 Done clicking all 'Add to Library' buttons!")
input("Press Enter to close...")
driver.quit()
