from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import argparse
from generator import generate_fake_credential

# ✅ Argument Handling
parser = argparse.ArgumentParser(description="Automate login attempts with Selenium")
parser.add_argument("--url", type=str,default="https://voting.name.ng/slink/vote-ig-fashion_Ik-v/login",help="Target login page URL")
parser.add_argument("--count", type=int, default=1, help="Number of times to run")
args = parser.parse_args()

# ✅ Update ChromeDriver path
CHROME_DRIVER_PATH = r"C:\Users\gokul\Desktop\Gokul Github\phishhunter\chromedriver.exe"

# ✅ Initialize WebDriver
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

# ✅ Number of times to run
#count = int(input("Enter the number of times to run: "))

# ✅ Define 6-digit OTP generator function
def generate_6_digit_code():
    return random.randint(100000, 999999)

# ✅ Loop through credentials
for i in range(args.count):
    username, password = generate_fake_credential()
    print(f"🔄 Trying credential {i+1}: {username}")

    driver.get(args.url)

    try:
        # ✅ Wait for the input fields
        username_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "user_name"))  # Ensure correct field name
        )
        password_input = driver.find_element(By.NAME, "user_age")  # Ensure correct field name
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # ✅ Fill credentials
        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        # ✅ Submit the form
        login_button.click()

        time.sleep(5)  # Allow time for response

        # ✅ Handle Two-Factor Authentication (2FA)
        try:
            two_fa_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "user_otp"))  # Ensure correct field name
            )

            two_fa_code = generate_6_digit_code()  # Generate OTP
            two_fa_input.send_keys(two_fa_code)

            continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            continue_button.click()

            print(f"✅ 2FA code {two_fa_code} submitted for {username}")
            time.sleep(5)  # Wait for login confirmation

        except Exception:
            print(f"⚠️ No 2FA required for {username}")

        # ✅ Check if login was successful
        if "login" in driver.current_url:
            print(f"❌ Login failed for {username}")
        else:
            print(f"✅ Login successful for {username}")

    except Exception as e:
        print(f"⚠️ Error with {username}: {e}")

    time.sleep(2)  # Prevent rate limiting

driver.quit()
