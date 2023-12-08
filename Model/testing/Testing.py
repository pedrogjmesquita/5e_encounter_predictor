import random
import time
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pickle
import os
from utils import encode_and_normalize_Data, predict_difficulty,predict_tpk, confidence_interval_sample, input_data

new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
m = len(new_data)-1
results = []
for i in range(m):

    new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
    n = random.randint(0, len(new_data)-1)
    escolha = input(f'Modo (1-auto|2-manual): ')
    
    if escolha == '1':
        input_data = new_data.iloc[i].T.to_frame().T
    else:
        input_data = pd.DataFrame(input_data(), index=[0])
        print(new_data)

    with open('Model/encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    with open('Model/normalizer.pkl', 'rb') as f:
        normalizer = pickle.load(f)


    data_encoded_normalized = encode_and_normalize_Data(input_data, encoder, normalizer)

    regression_prediction = predict_difficulty(data_encoded_normalized)
    classification_prediction = predict_tpk(data_encoded_normalized)
    expected = round(float(new_data['dificulty'].values[0]),3)

    print(f'Prediction: dificulty: {regression_prediction}\tPossible TPK: {classification_prediction}')
    print(f'Expected: dificulty: {expected}')
    time.sleep(5)
    error = (regression_prediction - expected)
    if(error > 1):
        time.sleep(1000)
        print(new_data)
    results.append(error)
    os.system('cls')
    print("Simulating: ")
    print(f"{i}/{m}")

mean = np.mean(results)
max = np.max(results)
min = np.min(results)
std = np.std(results)
print(f'Number of tests: {len(results)}')
print(f'Average error: {mean}')
print(f'Max error: {max}')
print(f'Min error: {min}')
print(f'Standard deviation: {std}')


# plt.hist(results, bins=20)
# plt.show()
plt.hist(results, bins='auto')
plt.show()
pd.DataFrame(results).to_csv('Data/RegressionModelErrorsNonAbsolute.csv', index=False, header='Error')
