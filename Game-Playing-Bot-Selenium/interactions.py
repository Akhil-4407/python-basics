from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--guest")
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

entries = driver.find_elements(By.CLASS_NAME,value="form-control")
entries[0].send_keys("AKhil")
entries[1].send_keys("K")
entries[2].send_keys("akhil.k.hlc0008@gmail.com")

submit = driver.find_element(By.CLASS_NAME,value="btn")
submit.send_keys(Keys.ENTER)
# driver.quit()