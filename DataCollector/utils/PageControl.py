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
        driver.find_element(By.XPATH, add_player_button).click()
        
        # select player class
        driver.find_element(By.XPATH, classes_buttons[player["class"]]).click()
        
        # select player level
        driver.find_element(By.XPATH, level_buttons[player["level"]]).click()

        # open custom player tab 
        driver.find_element(By.XPATH, add_player_custom).click()

        # set player hitpoints
        hitpoints_field = driver.find_element(By.XPATH, add_player_hitpoints)
        hitpoints_field.clear()
        hitpoints_field.send_keys(player["hitpoints"])

        # set player armour class
        armour_class_field = driver.find_element(By.XPATH, add_player_armour_class)
        armour_class_field.clear()
        armour_class_field.send_keys(player["armour_class"])

        # set player average save
        avg_save_field = driver.find_element(By.XPATH, add_player_avg_save)
        avg_save_field.clear()
        avg_save_field.send_keys(player["avg_save"])

        # confirm player
        driver.find_element(By.XPATH, add_player_ok_button).click()


    def addEnemies(driver:webdriver, enemy:dict):
        '''
        add the enemies to the webpage
        I: driver: WebDriver, the browser; player: dict, the player
        O: None
        '''
        
        # add enemy
        driver.find_element(By.XPATH, add_enemy).click()
    
        # set enemy name
        name_field = driver.find_element(By.XPATH, enemy_name_input)
        name_field.clear()
        name_field.send_keys(enemy['name'])

        # click searched enemy
        driver.find_element(By.XPATH, select_searched_enemy).click()    

        # confirm enemy
        driver.find_element(By.XPATH, add_enemy_ok_button).click()

        # set number of enemies
        num_field = driver.find_element(By.XPATH, num_enemy_input)
        num_field.clear()
        num_field.send_keys(enemy['num_enemies'])



