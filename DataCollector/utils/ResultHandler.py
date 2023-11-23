from selenium.webdriver.common.by import By

from time import sleep

from utils.constants import WRITING_FILE


class ResultHandler:

    def getResults(driver,num_players):
        '''
        get the results from the simulation
        '''
        raw_result_set = ''
        for i in range(1,20):
            try:
                raw_result_set = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div[1]/div[2]/div[2]/div[{i}]')
            except:
                raw_result_set = driver.find_element(By.XPATH, f'//*[@id="__next"]/main/div[1]/div[2]/div[2]/div[{i-1}]')
                break
        result_set = ResultHandler.parseResults(raw_result_set.text, num_players)
        return ResultHandler.lifeFraction(result_set)


    def parseResults(raw_result_set, num_players):
        '''
        parse the results from the simulation
        I: raw_result_set: string, the raw results from the simulation; num_players: int, the number of players
        O: raw_players_life: list<string>, the raw life of each player
        '''

        raw_players_life = []
        raw_result_set = raw_result_set.split('\n')
        for i in range(num_players):
            raw_players_life.append(raw_result_set[2*i+1])
        return raw_players_life
       

    def lifeFraction(lifes:list):
        '''
        convert the hp from fractions in string form ("x/y") to a int, and sum them up
        I: lifes: list<string>, the life of each player
        O: life_fraction: string, the fraction of life remaining
        '''
        top_sum = 0
        bottom_sum = 0
        try:
            for life in lifes:
                
                if '+' in life:
                    life = ResultHandler.handleLifeWithModifier(life)

                life = life.split('/')
                x_i = int(life[0])
                y_i = int(life[1])

                top_sum += x_i/(y_i**2)
                bottom_sum += 1/(y_i)

        except:
            print("READING ERROR...")
            return -1
        return top_sum/bottom_sum
    
    def handleLifeWithModifier(life):
        '''
        handles the HPs that have a modifier by them
        I: life: string, the life of the player ("x/y+z")
        O: life: string, the life of the player ("x+z/y")
        '''
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
        '''
        write the results to a .csv file
        I: players: list<dict>, the list of players; enemies: dict, the enemies; life_results: string, the fraction of life remaining
        O: None
        '''
        result = ''
        for player in players:
            result += f'{player["class"]},{player["level"]},{player["hitpoints"]},{player["armour_class"]},{player["avg_save"]},'

        with open(WRITING_FILE, 'a') as f:
            result += f'{enemies.num_enemies},{enemies.name},{enemies.cr},{enemies.ac},{enemies.hp},{enemies.type},{life_results}'
            f.write(f'\n{result}')
            f.close()
        
        print(result)


