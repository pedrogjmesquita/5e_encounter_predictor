from random import randint

from utils.constants import classes, hitdice, armour_classes_range


class Players:

    # initializes the group of players
    def __init__(self,num_players):
        self.num_players = num_players
        self.players = []
        self.players_level = randint(1, 5)
        self.create_players()
        self.hp_generator(self.players)
        self.armour_class_generator(self.players)
    
    def create_players(self):
        '''
        creates the players list
        I: None
        O: None
        '''
        for _ in range(self.num_players):
            self.players.append(self.create_player())

    def create_player(self):
        '''
        creates a simgle random player
        I: None
        O: player: dict, the player
        '''
        player = {
            "class": classes[randint(0,12)],
            "level": self.players_level,
            "hitpoints": None,
            "armour_class":  None,
            "avg_save": 2 if self.players_level < 3 else 3
        }
        return player

    def hp_generator(self,players):
        '''
        generates the hitpoints for each player based on their class and level
        I: players: list<dict>, the list of players
        O: None        
        '''
        for player in players:
            modifier = randint(0, 3)
            hitdie = hitdice[player["class"]]
            rolled_life = 0
            for i in range(player["level"]):
                dice_roll = randint(hitdie/2 , hitdie)
                rolled_life += dice_roll + modifier
            player["hitpoints"] = rolled_life

    def armour_class_generator(self,players):
        '''
        generates the armour class for each player based on their class and level
        I: players: list<dict>, the list of players
        O: None        
        '''
        for player in players:
            player["armour_class"] = randint(armour_classes_range[player["class"]][0], armour_classes_range[player["class"]][1])
