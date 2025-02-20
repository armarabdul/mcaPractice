# import selenium
# print(selenium.__version__)
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#  # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(3)
#  # Navigate to the form page
# driver.get('https://www.confirmtkt.com/pnr-status')
#  # Locate form elements
# pnr_field = driver.find_element("name", "pnr")
# submit_button = driver.find_element(By.CSS_SELECTOR, '.col-xs-4')
#  # Fill in form fields
# pnr_field.send_keys('4358851774')
#  # Submit the form
# submit_button.click()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Start WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.confirmtkt.com/pnr-status")  # Example URL
# driver.maximize_window()

# # Locate the PNR input field
# pnr_field = driver.find_element(By.NAME, "pnr")

# # Enter PNR number
# pnr_field.send_keys("4358851774")

# # Submit the form (if inside a <form> tag)
# pnr_field.submit()

# # Wait for the results to load
# time.sleep(5)

# # Close the browser
# driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#  # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(3)
#  # Navigate to the form page
# driver.get('https://www.confirmtkt.com/pnr-status')
#  # Locate form elements
# pnr_field = driver.find_element("name", "pnr")
# submit_button = driver.find_element(By.CSS_SELECTOR, '.col-xs-4')
# # Fill in form fields
# pnr_field.send_keys('4358851774')
#  # Submit the form
# submit_button.click()
# welcome_message = driver.find_element(By.CSS_SELECTOR,".pnr-card")
#  # Print or use the scraped values
# print(type(welcome_message))
# html_content = welcome_message.get_attribute('outerHTML')
#  # Print the HTML content
# print("HTML Content:", html_content)
#  # Close the browser
# driver.quit()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
# driver.maximize_window()
# time.sleep(3)

# # Open the Google Form
# driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeOEoUjvv7W7EE_PFG6S8130NSlzdWkFSE7UrXppzdyjC2g/viewform")

# # Locate the input fields using XPath
# name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
# col = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/input')
# sel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[2]/label/div/div[2]/div/span')
# submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

# # Fill out the form
# name.send_keys("Ekant")
# col.send_keys("RNSIT")
# sel.click()
# submit.click()

# # Close the driver after submission
# time.sleep(2)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# # Locate the search input field
# search_box = driver.find_element(By.NAME, "q")

# # Enter a search query
# search_box.send_keys("Selenium Python tutorial")

# # Submit the form using ENTER key
# search_box.send_keys(Keys.RETURN)

# # Wait for results to load
# time.sleep(3)

# # Print the title of the results page
# print(driver.title)

# # Close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.confirmtkt.com/pnr-status")

# Wait for page to load
time.sleep(2)

# Locate PNR input field and submit button
pnr_field = driver.find_element(By.NAME, "pnr")
submit_button = driver.find_element(By.CSS_SELECTOR, ".col-xs-4")

# Enter a sample PNR number and submit
pnr_field.send_keys("4358851774")
submit_button.click()

# Wait for results to load
time.sleep(5)

# Save the page HTML after form submission
html_content = driver.page_source
with open("pnr_status.html", "w", encoding="utf-8") as file:
    file.write(html_content)

# Close the browser
driver.quit()
