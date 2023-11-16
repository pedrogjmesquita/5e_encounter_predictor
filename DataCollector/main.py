from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import accept_cookies_button

from utils import PageControl
from utils import Players



# create a new Chrome browser instance
driver = webdriver.Edge()

# navigate to Google search
driver.get("https://battlesim-zeta.vercel.app/")
sleep(3)

# accept cookies
driver.find_element(By.XPATH, accept_cookies_button).click()

# players = Players(4)

# for player in players.players:
#     PageControl.addPlayer(driver, player)
#     PageControl.creatureAddedLog(player)

driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div[1]/button').click()
table = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/div')
enimies = table.text.split("\n")
print(enimies)
sleep(5)
# close the browser
driver.quit()
