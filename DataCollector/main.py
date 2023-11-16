from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import accept_cookies_button, reset_button

from utils import Players, Enemies, PageControl, ResultHandler, creatureAddedLog


# create a new Chrome browser instance
driver = webdriver.Edge()

# navigate to Google search
driver.get("https://battlesim-zeta.vercel.app/")
sleep(3)

# accept cookies
driver.find_element(By.XPATH, accept_cookies_button).click()

while(True):

    st = time.time()
    players = Players(4)

    for player in players.players:
        PageControl.addPlayer(driver, player)
        creatureAddedLog(player)

    enemies = Enemies(players.players[0]['level'])
    PageControl.addEnemy(driver, enemies.enemies)

    ResultHandler.getResults(driver, 4)
    et = time.time()

    print(f"Time elapsed: {et - st}")
    sleep(10)
    driver.find_element(By.XPATH, reset_button).click()
# close the browser
driver.quit()
