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

    def addEnemy(driver, enemy):
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
            "class": classes[randint(0,12)],
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
    def __init__(self,level):
        self.players_level = level
        self.create_enemie()
        self.num_enemies = self.set_num_enemies()
        
        self.enemies = {
            "num_enemies": self.num_enemies,
            "name": self.name,
            "cr": self.cr,
            "hp": self.hp,
            "ac": self.ac
        }

    def create_enemie(self):
        df = read_csv('Data/enemies_under_14_final.csv')
        random_enemy = randint(0, len(df['name'])-1)
        self.name = df['name'][random_enemy]
        self.cr = df['cr'][random_enemy]
        self.hp = df['hp'][random_enemy]
        self.ac = df['ac'][random_enemy]

    def set_num_enemies(self):
        num_enemies = 1
        limits = self.set_trerhold_based_on_level()
        treshhold = randint(limits[0], limits[1])
        if(self.cr == 0): 
            return 10
        while(self.cr*num_enemies < treshhold and num_enemies < 20):
            num_enemies += 1
        return num_enemies
    
    def set_trerhold_based_on_level(self):
        if(self.players_level == 1):
            return [0,4]
        elif(self.players_level == 2):
            return [1,5]
        elif(self.players_level == 3):
            return [2,10]
        elif(self.players_level == 4):
            return [3,12]
        else:
            return [4,18]

class ResultHandler:
    def getResults(driver,num_players):
        raw_result_set = ''
        for i in range(1,10):
            try:
                raw_result_set = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div[1]/div[2]/div[2]/div[{i}]')
            except:
                raw_result_set = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div[1]/div[2]/div[2]/div[{i-1}]')
                break
        result_set = ResultHandler.parseResults(raw_result_set.text, num_players)
        return ResultHandler.lifeFraction(result_set)


    def parseResults(raw_result_set, num_players):
        raw_players_life = []
        raw_result_set = raw_result_set.split('\n')
        for i in range(num_players):
            raw_players_life.append(raw_result_set[2*i+1])
        return raw_players_life
        
    def lifeFraction(lifes:list):
        remaining_life = 0
        total_life = 0
        try:
            for life in lifes:
                
                if '+' in life:
                    life = ResultHandler.handleLifeWithModifier(life)

                life = life.split('/')
                remaining_life += int(life[0])
                total_life += int(life[1])
        except:
            print(lifes)
        return f'{remaining_life}/{total_life}'
    
    def handleLifeWithModifier(life):
        life = life.split('/')
        top_life = int(life[0])
        bottom_life = int(life[1].split('+')[0])
        modifier = int(life[1].split('+')[1])
        if top_life == 0:
            pass
        elif top_life + modifier > bottom_life:
            top_life = bottom_life
        else:
            top_life = top_life + modifier
        return f'{top_life}/{bottom_life}'
    
    def writeResults(players, enemies, life_results):
        life_fraction = float(life_results.split('/')[0])/float(life_results.split('/')[1])
        result = ''
        for player in players:
            result += f'{player["class"]},{player["level"]},{player["hitpoints"]},{player["armour_class"]},{player["avg_save"]},'

        with open('results.csv', 'a') as f:
            f.write(f'{result}{enemies.name},{enemies.cr},{enemies.ac},{enemies.hp},{life_fraction} \n')
            f.close()


