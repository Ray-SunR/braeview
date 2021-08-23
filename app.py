from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
import traceback 

driver = webdriver.Chrome()
while True:
	try:
		driver.get("https://braeview.net/Account/UserLogin.aspx")
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cpUserAccountContent_username")))
		username = driver.find_element(by="id", value="cpUserAccountContent_username")
		password = driver.find_element(by="id", value="cpUserAccountContent_password")
		login_button = driver.find_element(by="id", value="bLogin")
		username.clear()
		username.send_keys("\{\{YOUR_USERNAME\}\}")
		password.clear()
		password.send_keys("\{\{YOUR_PASS_WORD@\}\}")
		login_button.click()
		live_view = WebDriverWait(driver, 10).until(
					EC.presence_of_element_located((By.ID, "cSideNavMenu_liLiveView"))
			)
		live_view.click()
		video = driver.find_element(by=By.TAG_NAME, value="video")
		video.click()
			
		WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'An error has occurred')]")))
	except InvalidSessionIdException:
		print('retrying on invalid session id')
		driver = webdriver.Chrome()
	except:
		traceback.print_exc()
		driver.close()
