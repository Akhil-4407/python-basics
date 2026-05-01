from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
chrome_options = Options()
chrome_options.add_argument("--guest")
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


wait = WebDriverWait(driver,15)
element = wait.until(EC.element_to_be_clickable((By.ID,"langSelect-EN")))
element.click()

wait_cookie = WebDriverWait(driver,20)
cookie = wait_cookie.until(EC.element_to_be_clickable((By.ID,"bigCookie")))
curr = time.time()
timer = time.time() + 5*60
while curr <= timer:
    try:
        cookie.click()
    except ElementClickInterceptedException:
        print("Cookie not clicked this round...")
    except Exception as e:
        print("Some unexcepted exception occured...")
    time.sleep(0.01)
    if curr + 5 <= time.time():
        curr = time.time()
        store = driver.find_elements(By.CSS_SELECTOR,value=".product.unlocked.enabled")
        if store:
            try:
                store[-1].click()
            except ElementClickInterceptedException:
                print("Could not be clicked this time...")
            except TimeoutException:
                print("Took too long to respond")
