from selenium.webdriver.common.by import By
from selenium import webdriver

from utils.constants import *

class PageControl:

    def addPlayer(driver:webdriver, player:dict):
        '''
        add the players to the webpage
        I: driver: WebDriver, the browser; player: dict, the player
        O: None
        '''
        # add player
        driver.find_element(By.XPATH, ADD_PLAYER_BUTTON).click()
        
        # select player class
        driver.find_element(By.XPATH, CLASSES_BUTTONS[player["class"]]).click()
        
        # select player level
        driver.find_element(By.XPATH, LEVEL_BUTTONS[player["level"]]).click()

        # open custom player tab 
        driver.find_element(By.XPATH, ADD_PLAYER_CUSTOM).click()

        # set player hitpoints
        hitpoints_field = driver.find_element(By.XPATH, ADD_PLAYER_HITPOINTS)
        hitpoints_field.clear()
        hitpoints_field.send_keys(player["hitpoints"])

        # set player armour class
        armour_class_field = driver.find_element(By.XPATH, ADD_PLAYER_ARMOUR_CLASS)
        armour_class_field.clear()
        armour_class_field.send_keys(player["armour_class"])

        # set player average save
        avg_save_field = driver.find_element(By.XPATH, ADD_PLAYER_AVG_SAVE)
        avg_save_field.clear()
        avg_save_field.send_keys(player["avg_save"])

        # confirm player
        driver.find_element(By.XPATH, ADD_PLAYER_OK_BUTTON).click()


    def addEnemies(driver:webdriver, enemy:dict):
        '''
        add the enemies to the webpage
        I: driver: WebDriver, the browser; player: dict, the player
        O: None
        '''
        
        # add enemy
        driver.find_element(By.XPATH, ADD_ENEMY).click()
    
        # set enemy name
        name_field = driver.find_element(By.XPATH, ENEMY_NAME_INPUT)
        name_field.clear()
        name_field.send_keys(enemy['name'])

        # click searched enemy
        driver.find_element(By.XPATH, SELECT_SEARCHED_ENEMY).click()    

        # confirm enemy
        driver.find_element(By.XPATH, ADD_ENEMY_OK_BUTTON).click()

        # set number of enemies
        num_field = driver.find_element(By.XPATH, NUM_ENEMY_INPUT)
        num_field.clear()
        num_field.send_keys(enemy['num_enemies'])



