from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
def setup_selenium():
    chrome_options = Options()
    
    # Headless mode is disabled to allow the user to see the webpage
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--start-maximized')
    
    # Setup the download directory for PDFs
    prefs = {
        "download.default_directory": "/Users/abdul/Downloads/automated_pdfs",
        "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local"}],"selectedDestinationId":"Save as PDF","version":2}',
        "savefile.default_directory": "/Users/abdul/Downloads/automated_pdfs",
        "profile.default_content_settings.popups": 0,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "printing.default_destination_selection_rules": {
            "kind": "local",
            "namePattern": "Save as PDF"
        }
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--kiosk-printing')

    # Install the correct ChromeDriver version
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Fetch results
def fetch_results(usn_number):
    direct_url = "https://results.vtu.ac.in/DJcbcs24/index.php"

    driver = setup_selenium()

    try:
        print(f"Fetching results for USN: {usn_number}")

        # Step 1: Open the results page
        driver.get(direct_url)
        time.sleep(2)  # Allow the page to load

        # Step 2: Enter the USN
        usn_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "lns"))
        )
        usn_input.send_keys(usn_number)
        print(f"Entered USN: {usn_number}")

        # Wait for the user to manually solve the CAPTCHA and submit the form
        WebDriverWait(driver, 300).until(
            EC.url_contains("resultpage.php")
        )
        print("CAPTCHA solved and result page loaded.")

        # Step 3: Click the print button
        print_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='ಮುದ್ರಣ / PRINT']"))
        )
        print_button.click()
        print("Print button clicked.")

        # Allow time for the download to process
        time.sleep(5)

    except Exception as e:
        print(f"Error fetching results for USN {usn_number}: {e}")
    finally:
        driver.quit()

def main():
    # Loop over 25 USNs starting from "1BI22VL001"
    for i in range(1, 26):
        usn_number = f"1BI22VL{str(i).zfill(3)}"
        fetch_results(usn_number)

    print("Results fetched for all USNs.")

    for usn_number in usn_number:
        fetch_results(usn_number)

if __name__ == "__main__":
    main()
