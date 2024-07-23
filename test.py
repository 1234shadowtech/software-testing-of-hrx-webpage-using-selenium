import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time
import os

# Test results dictionary
test_results = {
    'Test Case': [],
    'Description': [],
    'Result': []
}

def add_test_result(test_case, description, result):
    test_results['Test Case'].append(test_case)
    test_results['Description'].append(description)
    test_results['Result'].append(result)

# Initialize the Chrome driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)  # Increased wait time

def execute_test_case(test_case, description, action):
    try:
        action()
        add_test_result(test_case, description, 'Passed')
    except Exception as e:
        add_test_result(test_case, description, f'Failed: {str(e)}')
        print(f"Error in {test_case}: {str(e)}")

def login(username, password):
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
    login_button.click()
    
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div/form/div[1]/div/div/div/input")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div/form/div[2]/div/div/div/input")))
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[2]/button")))
    submit_button.click()
    
    time.sleep(5)  # Wait for login to complete

try:
    # Test Case 1: Verify the title of the HRX homepage
    def test_case_1():
        driver.get("https://www.hrxbrand.com")
        time.sleep(10)  # Increased delay for page load
        expected_title = "HRX | HRX Brands"  # Updated expected title
        actual_title = driver.title
        print(f"Expected title: {expected_title}")
        print(f"Actual title: {actual_title}")
        assert expected_title == actual_title, "Title mismatch"

    execute_test_case('Test Case 1', 'Verify the title of the HRX homepage', test_case_1)

    # Test Case 2: Maximize the window
    def test_case_2():
        driver.maximize_window()

    execute_test_case('Test Case 2', 'Maximize the window', test_case_2)

    # Test Case 3: Login to the website
    def test_case_3():
        username = "7892113296"  # Replace with actual username
        password = "Preethu@123"  # Replace with actual password
        login(username, password)

    execute_test_case('Test Case 3', 'Login to the website', test_case_3)

    # Test Case 4: Navigate to Collection section
    def test_case_4():
        collection_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Collection')]")))
        driver.execute_script("arguments[0].click();", collection_section)
        time.sleep(5)

    execute_test_case('Test Case 4', 'Navigate to Collection section', test_case_4)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)

    # Test Case 5: Visit blog page
    def test_case_5():
        blog_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Blog')]")))
        driver.execute_script("arguments[0].click();", blog_link)
        time.sleep(5)

    execute_test_case('Test Case 5', 'Visit blog page', test_case_5)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)

    # Test Case 6: Navigate to HRX Hub page
    def test_case_6():
        hrx_hub = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'HRX Hub')]")))
        driver.execute_script("arguments[0].click();", hrx_hub)
        time.sleep(5)

    execute_test_case('Test Case 6', 'Navigate to HRX Hub page', test_case_6)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(2)

    # Test Case 7: Return back to home page
    def test_case_7():
        home_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Home')]")))
        driver.execute_script("arguments[0].click();", home_link)
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(5)

    execute_test_case('Test Case 7', 'Return to home page', test_case_7)

    # Test Case 8: Save test results to Excel file
    def test_case_8():
        test_results_df = pd.DataFrame(test_results)
        test_results_file_path = r"C:\ABC\work_hrx.xlsx"
        os.makedirs(os.path.dirname(test_results_file_path), exist_ok=True)
        test_results_df.to_excel(test_results_file_path, index=False)
        print(f"Test results saved to {test_results_file_path}")

    execute_test_case('Test Case 8', 'Save test results to Excel file', test_case_8)

except Exception as e:
    add_test_result('General Exception', f'An exception occurred during the test execution: {str(e)}', 'Failed')
    print(f"Error: {str(e)}")

finally:
    # Test Case 9: Close the website
    driver.quit()
    add_test_result('Test Case 9', 'Close the website', 'Passed')

    # Print the test results
    test_results_df = pd.DataFrame(test_results)
    print(test_results_df)

    # Save final test results to an Excel file
    test_results_file_path = r"C:\p\sow_test lab\test.py"
    try:
        os.makedirs(os.path.dirname(test_results_file_path), exist_ok=True)
        test_results_df.to_excel(test_results_file_path, index=False)
        print(f"Final test results saved to {test_results_file_path}")
    except Exception as e:
        print(f"Failed to save final test results to Excel: {str(e)}")

    # Calculate and display test case statistics
    total_test_cases = len(test_results['Test Case'])
    passed_test_cases = test_results['Result'].count('Passed')
    failed_test_cases = total_test_cases - passed_test_cases

    print(f"\nSummary:")
    print(f"Total Test Cases: {total_test_cases}")
    print(f"Test Cases Passed: {passed_test_cases}")
    print(f"Test Cases Failed: {failed_test_cases}")