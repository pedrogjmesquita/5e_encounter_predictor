from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import accept_cookies_button

from utils import Enemies, PageControl
from utils import Players



# create a new Chrome browser instance
driver = webdriver.Edge()

# navigate to Google search
driver.get("https://battlesim-zeta.vercel.app/")
sleep(3)

# accept cookies
driver.find_element(By.XPATH, accept_cookies_button).click()

players = Players(4)

for player in players.players:
    PageControl.addPlayer(driver, player)
    PageControl.creatureAddedLog(player)

enemies = Enemies(players.players[0]['level'])
PageControl.addEnemy(driver, enemies.enemies)

print(PageControl.getResults(driver))

sleep(10)

# close the browser
driver.quit()
