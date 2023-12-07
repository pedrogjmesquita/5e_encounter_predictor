import random
import time
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pickle
import os
from utils import confidence_interval_population, confidence_interval_sample



import xgboost as xgb
new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
m = len(new_data)-1
results = []
for i in range(m):
    model = xgb.XGBRegressor()
    model.load_model('Model\model_OPT_NORMALIZED.ubj')
    new_data = pd.read_csv('Data/test_sample.csv', encoding='utf-8')
    n = random.randint(0, len(new_data)-1)
    new_data = new_data.iloc[i].T.to_frame().T

    with open('Model/encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
    with open('Model/normalizer.pkl', 'rb') as f:
        normalizer = pickle.load(f)


    features_df = encoder.transform(new_data[['p1_class', 'p2_class', 'p3_class', 'p4_class', 'monster_type']])
    new_data_encoded = pd.concat([new_data, features_df], axis=1).drop(columns=['p1_class', 'p2_class', 'p3_class', 'p4_class', 'monster_type', 'monster_name','dificulty'])
    new_data_encoded_normalized = normalizer.transform(new_data_encoded)
    new_data_encoded_normalized = pd.DataFrame(new_data_encoded_normalized, columns=new_data_encoded.columns)

    # Use the model's predict method on the processed data

    df = pd.DataFrame(new_data_encoded_normalized.values , columns = model.feature_names_in_)

    prediction = model.predict(df)[0]
    expected = new_data['dificulty'].values[0]
    error = abs(prediction - expected)
    results.append(error)
    os.system('cls')
    print("Simulating: ")
    print(f"{i}/{m}")

print(f'Number of tests: {len(results)}')
print(f'Average error: {np.mean(results)}')
print(f'Max error: {np.max(results)}')
print(f'Min error: {np.min(results)}')
print(f'Standard deviation: {np.std(results)}')
print(f'Model error interval (with 99% confidence) using samples: {confidence_interval_sample(np.mean(results), np.std(results), len(results))}')
print(f'Model error interval (with 99% confidence) using population: {confidence_interval_population(np.mean(results), np.std(results), len(results))}')

plt.hist(results, bins=20)
plt.show()
plt.savefig('Images/RegressionModelErrors.png')
