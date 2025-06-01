from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure the browser
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Step 1: Manual login
driver.get("https://old.reddit.com/login")
input("[🔒] Inicia sesión en Reddit y presiona ENTER aquí...")

# Step 2: Go to the overview
driver.get("https://old.reddit.com/user/YOURUSERNAME/")

def borrar_elementos():
    while True:
        time.sleep(3)

        # Step 1: Click on all the "delete" links
        delete_links = driver.find_elements(By.XPATH, '//a[@data-event-action="delete"]')
        if not delete_links:
            print("✅ There are no more removable items on this page.")
            break

        for delete_link in delete_links:
            try:
                delete_link.click()
                time.sleep(0.5)

                # Step 2: Click the "yes" button to confirm.
                yes_button = driver.find_element(By.XPATH, '//a[@class="yes" and contains(@onclick, "del")]')
                yes_button.click()
                print("🗑️ Deleted.")
                time.sleep(1.5)
            except Exception as e:
                print("⚠️ Error deleting:", e)
                continue

        # Go to the next page if it exists
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".next-button a")
            next_button.click()
            print("➡️ Next page...")
        except:
            print("🏁 There are no more pages.")
            break

borrar_elementos()
driver.quit()
