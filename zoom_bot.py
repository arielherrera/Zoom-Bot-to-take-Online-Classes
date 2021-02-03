from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard
class zoom_bot:
	def join(self, meeting_link):
		try:
			driver = webdriver.Firefox()
			driver.get(meeting_link)
			driver.current_window_handle
			time.sleep(3)
			element = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div')
			driver.switch_to.frame(frame)
			driver.find_element(By.TAG_NAME, 'button').click()
		finally:
			driver.quit()
			# quit will:
			# close all windows and tabs associated with that Webdriver session
			# close the broswer process
			# close the background driver process

link = open("meeting_link.txt","r").read()
zoom_bot().join(link)
