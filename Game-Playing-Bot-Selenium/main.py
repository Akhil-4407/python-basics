from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--guest")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

time_year = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
year_list = [x.text for x in time_year]
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events_list = [x.text for x in events]
print(year_list)
print(events_list)



event_details = {x:y for x,y in zip(year_list,events_list)}
print(event_details)
driver.quit()