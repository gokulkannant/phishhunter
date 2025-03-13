from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import random
from generator import generate_fake_credential

# ✅ Update ChromeDriver path
CHROME_DRIVER_PATH = r"C:\Users\gokul\Desktop\Gokul Github\phishunter\chromedriver.exe"

# ✅ Load credentials
""" def load_credentials(file_path):
    credentials = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                credentials.append((row[0], row[1]))
    return credentials """

#credentials = load_credentials("credentials.csv")

# ✅ Initialize WebDriver
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

count=int(input("Enter the number of times to run"))

index = 1

# ✅ Loop through credentials
for i in range(count):

    username, password = generate_fake_credential()
    
    print(f"🔄 Trying credential {index}: {username}")

    driver.get("https://voting.name.ng/slink/vote-ig-fashion_Ik-v/login")

    index+=1

    try:
        # ✅ Wait for the username field to appear
        username_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "user_name"))
        )
        password_input = driver.find_element(By.NAME, "user_age")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # ✅ Fill in the credentials
        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        # ✅ Submit the form
        login_button.click()

        time.sleep(5)  # Wait for response

        # ✅ Handle Two-Factor Authentication (2FA)
        try:
            two_fa_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "user_otp"))  # Check the correct field name
            )

            def generate_6_digit_code():
                return random.randint(100000, 999999)
            
           
            
            two_fa_code = generate_6_digit_code()  # Generate code
            two_fa_input.send_keys(two_fa_code)

            continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            continue_button.click()

            print(f"✅ 2FA code submitted for {username}")

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

    time.sleep(2)

driver.quit()