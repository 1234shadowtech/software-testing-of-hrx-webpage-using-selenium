from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get("https://playvalorant.com/")
wait = web