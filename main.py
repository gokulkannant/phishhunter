import os
import time
import random
import argparse
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from generator import generate_fake_credential  # Ensure this module exists

# Load environment variables from .env file (optional)
load_dotenv()

# ✅ Parse Command-Line Arguments
parser = argparse.ArgumentParser(description="Automate login attempts with Selenium")
parser.add_argument("--url", type=str, default="https://voting.name.ng/slink/vote-ig-fashion_Ik-v/login", help="Target login page URL")
parser.add_argument("--count", type=int, default=1, help="Number of login attempts")
parser.add_argument("--headless", action="store_true", help="Run Chrome in headless mode")
args = parser.parse_args()

# ✅ Configure Selenium WebDriver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass bot detection

# Enable Headless Mode if specified
if args.headless:
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

# ✅ Initialize Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ✅ Function to generate a 6-digit OTP
def generate_6_digit_code():
    return str(random.randint(100000, 999999))

# ✅ Perform login attempts
for i in range(args.count):
    username, password = generate_fake_credential()
    print(f"🔄 Attempt {i+1}: Trying {username}")

    driver.get(args.url)

    try:
        # ✅ Locate input fields
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "user_name"))
        )
        password_input = driver.find_element(By.NAME, "user_age")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # ✅ Fill in credentials
        username_input.send_keys(username)
        password_input.send_keys(password)

        # ✅ Submit form
        login_button.click()
        time.sleep(random.uniform(3, 6))  # Randomized delay

        # ✅ Handle 2FA if required
        try:
            two_fa_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, "user_otp"))
            )
            otp_code = generate_6_digit_code()
            two_fa_input.send_keys(otp_code)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print(f"✅ 2FA code {otp_code} submitted for {username}")
        except:
            print(f"⚠️ No 2FA required for {username}")

        # ✅ Check login success
        if "login" in driver.current_url:
            print(f"❌ Login failed for {username}")
        else:
            print(f"✅ Login successful for {username}")

    except Exception as e:
        print(f"⚠️ Error with {username}: {e}")

    time.sleep(random.uniform(2, 5))  # Randomized delay before next attempt

# ✅ Close WebDriver
driver.quit()
print("✅ Script completed.")
