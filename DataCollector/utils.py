from random import randint
from time import sleep
from constants import *
from selenium.webdriver.common.by import By
from constants import hitdice, armour_classes_range, classes
from pandas import read_csv

class PageControl:
    def addPlayer(driver, player):

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

    def addEnemie(driver, enemie):
        pass

    def creatureAddedLog(creature):
        print(f"Adicionado um {creature['class']} de nível {creature['level']} com {creature['hitpoints']} pontos de vida e armour class de {creature['armour_class']}")

class Players():
    def __init__(self,num_players):
        self.num_players = num_players
        self.players = []
        self.players_level = randint(1, 5)
        self.create_players()
        self.hp_generator(self.players)
        self.armour_class_generator(self.players)
    
    def create_players(self):
        for i in range(self.num_players):
            self.players.append(self.create_player())

    def create_player(self):
        player = {
            "class": classes[randint(0, 11)],
            "level": self.players_level,
            "hitpoints": None,
            "armour_class":  None,
            "avg_save": 2 if self.players_level < 3 else 3
        }
        return player

    def hp_generator(self,players):
        for player in players:
            modifier = randint(0, 3)
            hitdie = hitdice[player["class"]]
            rolled_life = 0
            for i in range(player["level"]):
                dice_roll = randint(hitdie/2 , hitdie)
                rolled_life += dice_roll + modifier
            player["hitpoints"] = rolled_life

    def armour_class_generator(self,players):
        for player in players:
            player["armour_class"] = randint(armour_classes_range[player["class"]][0], armour_classes_range[player["class"]][1])

class Enemies():
    def __init__(self):
        self.create_enemie()
        self.num_enemies = self.set_num_enemies()
        print(f"Peguei {self.num_enemies} {self.name} de CR {self.cr} com {self.hp} pontos de vida e armour class de {self.ac}")       
    
    def create_enemie(self):
        df = read_csv('Data/enemies_under_14_final.csv')
        random_enemy = randint(0, len(df['name'])-1)
        self.name = df['name'][random_enemy]
        self.cr = df['cr'][random_enemy]
        self.hp = df['hp'][random_enemy]
        self.ac = df['ac'][random_enemy]

    def set_num_enemies(self):
        num_enemies = 1
        treshhold = randint(0,20)
        if(self.cr == 0): 
            return 10
        while(self.cr*num_enemies < treshhold):
            num_enemies += 1
        return num_enemies
