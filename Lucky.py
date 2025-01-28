import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import cv2
import numpy as np
from PIL import Image
import pytesseract
# Function to read accounts from a text file
def load_accounts(file_path):
    with open(file_path, "r") as file:
        accounts = [line.strip().split(",") for line in file.readlines()]
    return accounts

# Function to log in to an account
def login(driver, username, password):
    try:
        # Find and fill in the username field
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))  # Replace with the actual field name
        )
        username_field.clear()
        username_field.send_keys(username)

        # Find and fill in the password field
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))  # Replace with the actual field name
        )
        password_field.clear()
        password_field.send_keys(password)

        # Click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))  # Replace with actual button text
        )
        login_button.click()

        print(f"Logged in as {username}")
    except Exception as e:
        p0vrint(f"Failed to log in as {username}: {e}")


try(
# Load the image using OpenCV
image_path = "captcha_image.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save and read the processed image
processed_image_path = "processed_captcha.png"
cv2.imwrite(processed_image_path, thresh)
image = Image.open(processed_image_path)
)) catch(   )
# Extract text using pytesseract
captcha_text = pytesseract.image_to_string(image)

print(f"CAPTCHA Text: {captcha_text}")




        #Click faucet
        faucet = WebDriverWait(driver,10 ).until(
            EC.element_to_be_clickable(By.XPATH, "//FAUCET")
        )
        faucet.click()
        driver.send_keys(ESCAPE)

# Function uuto perform the coin-flipping game
def play_coin_flip_game(driver):
    wins = 0
    amount = 0.03
    total_flips = 0

    while wins < 10:
        total_flips += 1

        # Randomly select "Head" or "Tail"
        choice = random.choice(["Head", "Tail"])
        print(f"Flip {total_flips}: Selecting {choice}")

        try:
            # Find the button for the current choice
            button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{choice}')]"))
            )
            button.click()
            time.sleep(2)  # Wait for the result to update

            # Check for win/loss (adjust based on site behavior)
            result_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='result']"))  # Replace with actual result element
            )
            result = result_element.text.lower()  # Get the result (e.g., "win" or "lose")

            if "win" in result:
                wins += 1
                amount *= 2  # Double the amount on win
                print(f"Win! Total Wins: {wins}, Total Amount: {amount:.2f}")
            else:
                print(f"Loss. Total Amount: {amount:.2f}")

        except TimeoutException:
            print("Error: Button not found or not clickable.")
        except ElementNotInteractableException:
            print("Error: Button is not interactable.")

        # Optional: Add a short delay to prevent issues with rapid requests
        time.sleep(1)

    print("10 wins achieved!")

# Main program
if __name__ == "__main__":
    # Load accounts from the file
    accounts = load_accounts("accounts.txt")

    # Path to your WebDriver
    driver_path = "/path/to/chromedriver"  # Replace with your WebDriver path

    for account in accounts[:8]:  # Limit to the first 8 accounts
        username, password = account
        driver = webdriver.Chrome(driver_path)  # Start a new browser session
        driver.get("https://luckybird.io")  # Replace with the actual site URL

        try:
            # Log in and play the game
            login(driver, username, password)
            play_coin_flip_game(driver)
        finally:
            driver.quit()  # Close the browser

    print("All accounts processed!")
