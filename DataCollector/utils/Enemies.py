from pandas import read_csv

from random import randint

from utils.constants import MAX_CR_PER_LEVEL, MAX_NUM_OF_ENEMIES


class Enemies():

    # initializes the group of enemies
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

    # creates a random enemy and get it's stats
    def create_enemie(self):
        df = read_csv('Data/enemies_under_14_final.csv')
        random_enemy = self.get_random_enemy(df)
        self.name = df['name'][random_enemy]
        self.cr = df['cr'][random_enemy]
        self.hp = df['hp'][random_enemy]
        self.ac = df['ac'][random_enemy]
        self.type = df['type'][random_enemy]

    def get_random_enemy(self,df):
        cr = 99
        while(cr >= MAX_CR_PER_LEVEL[self.players_level-1]):
            random_enemy = randint(0, len(df['name'])-1)
            cr = df['cr'][random_enemy]
        return random_enemy

    # sets the number of enemies based on the players level and the enemies CR
    def set_num_enemies(self):
        num_enemies = 1
        limits = self.set_multiplier_trerhold_based_on_level()
        treshhold = randint(limits[0], limits[1])
        if(self.cr <= 0.5): 
            return 10
        while(self.cr*num_enemies < treshhold and num_enemies < MAX_NUM_OF_ENEMIES):
            num_enemies += 1
        return num_enemies
    
    # sets the treshhold for the CR*num_monster product, based on the players level
    def set_multiplier_trerhold_based_on_level(self):
        if(self.cr == MAX_CR_PER_LEVEL[self.players_level-1]):
            return [1,1]
        if(self.players_level == 1):
            return [0,2]
        elif(self.players_level == 2):
            return [1,4]
        elif(self.players_level == 3):
            return [1,9]
        elif(self.players_level == 4):
            return [1,12]
        else:
            return [1,20]
        
    