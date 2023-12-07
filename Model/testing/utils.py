import numpy as np


def input_data():
    # Input data
    print("Please input the following data:")
    level = int(input("Level: "))
    player_data = [{},{},{},{}]
    for i in range(4):
        print(f"\n==========Player {i+1}==========\n")
        player_data[i]['Hitpoints'] = int(input("Hitpoints: "))
        player_data[i]['Class'] = input("Class: ").capitalize()
        player_data[i]['ac'] = int(input("AC: "))
        player_data[i]['avg_save'] = 2 if level < 4 else 3
        print("\n================================\n")
    print("\n==========Enemies==========\n")
    num_enemies = int(input("Number of enemies: "))
    enemies_cr = int(input("Enemies CR: "))
    enemies_ac = int(input("Enemies AC: "))
    enemies_hitpoints = int(input("Enemies Hitpoints: "))
    enemies_type = input("Enemies Type: ").lower()

    data = {
        'level': level,
        'p1_class': player_data[0]['Class'],
        'p1_hp': player_data[0]['Hitpoints'],
        'p1_ac': player_data[0]['ac'],
        'p1_avg_save': player_data[0]['avg_save'],
        'p2_class': player_data[1]['Class'],
        'p2_hp': player_data[1]['Hitpoints'],
        'p2_ac': player_data[1]['ac'],
        'p2_avg_save': player_data[1]['avg_save'],
        'p3_class': player_data[2]['Class'],
        'p3_hp': player_data[2]['Hitpoints'],
        'p3_ac': player_data[2]['ac'],
        'p3_avg_save': player_data[2]['avg_save'],
        'p4_class': player_data[3]['Class'],
        'p4_hp': player_data[3]['Hitpoints'],
        'p4_ac': player_data[3]['ac'],
        'p4_avg_save': player_data[3]['avg_save'],
        'num_of_monsters': num_enemies,
        'monster_cr': enemies_cr,
        'monster_ac': enemies_ac,
        'monster_hp': enemies_hitpoints,
        'monster_type': enemies_type
    }
    
    return data

def confidence_interval_sample(mean, std, n):
    t = 2.326 # 99% confidence interval with (n-1)->inf
    lower = mean - t * std / np.sqrt(n)
    upper = mean + t * std / np.sqrt(n)
    return [lower, upper]

def confidence_interval_population(mean, std, n):
    z = 2.575 # 99% confidence interval with (n-1)->inf
    lower = mean - z * std / np.sqrt(n)
    upper = mean + z * std / np.sqrt(n)
    return [lower, upper]