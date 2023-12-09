import random
import time
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pickle
import os
from utils import encode_and_normalize_Data, predict_difficulty,predict_tpk, confidence_interval_sample, input_data # type: ignore

new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
escolha = input(f'Modo (1-auto|2-manual): ')

if escolha == '2':
    with open('Model/encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    with open('Model/normalizer.pkl', 'rb') as f:
        normalizer = pickle.load(f)
    input_data = pd.DataFrame(input_data(), index=[0])
    data_encoded_normalized = encode_and_normalize_Data(input_data, encoder, normalizer)

    regression_prediction = predict_difficulty(data_encoded_normalized)
    classification_prediction = predict_tpk(data_encoded_normalized)
    print(f'For a party of 4 players {input_data["players_level"].values[0]} level, wich are {input_data["p1_class"].values[0]}, {input_data["p2_class"].values[0]}, {input_data["p3_class"].values[0]}, {input_data["p4_class"].values[0]}')
    print(f'against {input_data["num_of_monsters"].values[0]} monster type {input_data["monster_type"].values[0]} of CR {input_data["monster_cr"].values[0]} with {input_data["monster_hp"].values[0]} HP and {input_data["monster_ac"].values[0]} AC')
    print(f'Prediction: dificulty: {regression_prediction}\tPossible TPK: {classification_prediction}')

else:
    num_of_errors = 0
    errors = []
    m = len(new_data)-1

    for i in range(m):

        new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
        n = random.randint(0, len(new_data)-1)
        new_data = new_data.iloc[n].T.to_frame().T

        with open('Model/encoder.pkl', 'rb') as f:
            encoder = pickle.load(f)
        with open('Model/normalizer.pkl', 'rb') as f:
            normalizer = pickle.load(f)


        data_encoded_normalized = encode_and_normalize_Data(new_data, encoder, normalizer)

        regression_prediction = predict_difficulty(data_encoded_normalized)
        classification_prediction = bool(predict_tpk(data_encoded_normalized))
        expected = round(float(new_data['dificulty'].values[0]),3)

        print(f'Prediction: dificulty: {regression_prediction}\tPossible TPK: {bool(classification_prediction)}')
        print(f'Expected: dificulty: {expected}\t Was TPK: {not(bool(expected))}')
        if(((not classification_prediction) and ( not bool(expected))) and (abs(regression_prediction - expected)>0.2)):
            print('Catastroficy error!')
            num_of_errors += 1
            errors.append(i)
        
        os.system('cls')
        print("Simulating: ")
        print(f"{i}/{m}")

    print(f'Number of errors: {num_of_errors}')
    print(f'Errors: {errors}')
