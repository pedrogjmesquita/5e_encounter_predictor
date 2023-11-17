# This file contains all the constants used in the project

hitdice = {
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

armour_classes_range = {
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

classes = [
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



accept_cookies_button = '//*[@id="__next"]/main/div[2]/div/button[1]'
add_player_button = '//*[@id="__next"]/main/div[1]/div[1]/button'
add_player_ok_button = '//*[@id="__next"]/main/div[1]/div[2]/div/div[3]/button[1]'
classes_links = [f'//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[1]/button[{i}]' for i in range(1, 14)]
classes_buttons = {classes[i]: classes_links[i] for i in range(len(classes))}
level_buttons = [f'//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[2]/button[{i}]' for i in range(6)]
add_player_custom = '//*[@id="__next"]/main/div[1]/div[2]/div/div[1]/button[3]'
add_player_hitpoints = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[2]/input'
add_player_armour_class = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[3]/input'
add_player_avg_save = '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/section[4]/input'
add_enemy = '//*[@id="__next"]/main/div[1]/div[2]/div[1]/button'
enemy_name_input = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/section[1]/input'
select_searched_enemy = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/button[1]'
add_enemy_ok_button = '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[3]/button[1]'
num_enemy_input = '//*[@id="__next"]/main/div[1]/div[2]/div[1]/div[2]/div[1]/div/span[2]/input'
reset_button = '//*[@id="__next"]/main/div[1]/div[1]/div[2]/div[2]/button[1]'
