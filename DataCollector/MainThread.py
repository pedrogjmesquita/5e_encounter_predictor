from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from utils.Players import Players
from utils.Enemies import Enemies
from utils.PageControl import PageControl
from utils.ResultHandler import ResultHandler
from utils.constants import ACCEPT_COOKIES_BUTTON, RESET_BUTTON

def execute():
    '''
    main function
    '''
    # create a new Edge browser instance
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)


    

    # navigate to the website
    driver.get("https://battlesim-zeta.vercel.app/")
    time.sleep(3)

    # accept cookies
    driver.find_element(By.XPATH, ACCEPT_COOKIES_BUTTON).click()

    # main scrapping loop
    while(True):

        try:
            # create the PCs
            players = Players(4)

            # add the PCs to the website
            for player in players.players:
                PageControl.addPlayer(driver, player)

            # time.sleep(10)

            # create the enemies
            enemies = Enemies(players.players[0]['level'])

            
            # add the enemies to the website
            PageControl.addEnemies(driver, enemies.enemies)

            # get the results from the simulation
            life_results = ResultHandler.getResults(driver, 4)

            # write the results to a file
            ResultHandler.writeResults(players.players, enemies, life_results)
            
            # reset the website, getting ready for the next loop
            driver.find_element(By.XPATH, RESET_BUTTON).click()
        except:
            print("ERROR...")
            break

    # close the browser
    driver.quit()

if __name__ == "__main__":
    execute()