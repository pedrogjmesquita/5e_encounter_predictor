from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from utils.Players import Players
from utils.Enemies import Enemies
from utils.PageControl import PageControl
from utils.ResultHandler import ResultHandler
from utils.constants import accept_cookies_button, reset_button

def execute():
    '''
    main function
    '''
    # create a new Edge browser instance
    # options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Edge(options=options)

    driver = webdriver.Edge()

    

    # navigate to the website
    driver.get("https://battlesim-zeta.vercel.app/")
    time.sleep(3)

    # accept cookies
    driver.find_element(By.XPATH, accept_cookies_button).click()

    # main scrapping loop
    while(True):

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

        time.sleep(10)
        # get the results from the simulation
        life_results = ResultHandler.getResults(driver, 4)

        # write the results to a file
        ResultHandler.writeResults(players.players, enemies, life_results)
        
        # reset the website, getting ready for the next loop
        driver.find_element(By.XPATH, reset_button).click()

        
    # close the browser
    driver.quit()

execute()