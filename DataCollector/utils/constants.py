# This file contains all the constants used in the project

MAX_NUM_OF_ENEMIES = 15

HITDICE = {
    'Artificer': 8,
    'Barbarian': 12,
    'Bard': 8,
    'Cleric': 8,
    'Druid': 8,
    'Fighter': 10,
    'Monk': 8,
    'Paladin': 10,
    'Ranger': 10,
    'Rogue': 8,
    'Sorcerer': 6,
    'Warlock': 8,
    'Wizzard': 6
}

ARMOUR_CLASSES_RANGE = {
    "Artificer": [12, 18],
    "Barbarian": [12, 17],
    "Bard": [12, 16],
    "Cleric": [12, 20],
    "Druid": [11, 16],
    "Fighter": [12, 19],
    "Monk": [10, 16],
    "Paladin": [14, 19],
    "Ranger": [12, 17],
    "Rogue": [11, 17],
    "Sorcerer": [10, 15],
    "Warlock": [11, 16],
    "Wizzard": [10, 15]
}

CLASSES = [
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizzard"
]

MAX_CR_PER_LEVEL = [
    5,
    8,
    9,
    10,
    13
]





ACCEPT_COOKIES_BUTTON = '//*[@id="__next"]/main/div[2]/div/button[1]'
ADD_PLAYER_BUTTON = '//*[@id="__next"]/main/div[1]/div[1]/button'
ADD_PLAYER_OK_BUTTON = '//*[@id="__next"]/main/div[1]/div[2]/div/div[3]/button[1]'
CLASSES_LINKS = [f'//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[1]/button[{i}]' for i in range(1, 14)]
CLASSES_BUTTONS = {CLASSES[i]: CLASSES_LINKS[i] for i in range(len(CLASSES))}
LEVEL_BUTTONS = [f'//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[2]/button[{i}]' for i in range(6)]
ADD_PLAYER_CUSTOM = '//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/button[3]'
ADD_PLAYER_HITPOINTS = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[2]/input'
ADD_PLAYER_ARMOUR_CLASS = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[3]/input'
ADD_PLAYER_AVG_SAVE = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[4]/input'
ADD_ENEMY = '//*[@id="__next"]/main/div[1]/div[2]/div[1]/button'
ENEMY_NAME_INPUT = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/section[1]/input'
SELECT_SEARCHED_ENEMY = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/button[1]'
ADD_ENEMY_OK_BUTTON = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[3]/button[1]'
NUM_ENEMY_INPUT = '//*[@id="__next"]/main/div[1]/div[2]/div[1]/div[2]/div[1]/div/span[2]/input'
RESET_BUTTON = '//*[@id="__next"]/main/div[1]/div[1]/div[2]/div[2]/button[1]'
