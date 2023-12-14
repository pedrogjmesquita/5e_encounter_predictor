# 5e Combat Predictor

This is a D&D 5th Edition Combat Ecounter Predictor using Machine Learning algorithms. The goal is to predict the outcome of a combat encounter based on the stats of the players and the monsters, classifying the encounter using the weighted average of the players' remaining hitpoints after the encounter.

The project consists of two separate XGBoost models, both using the same dataset, one regressor to predict the aproximate score of the encounter, and one classifier to classify the encounter as been a TPK (Total Party Kill) or a victory for the players. The difficulty of the encounter is a score from 0-1, beeing 0 a TPK and 1 a victory for the players, where they didn't take any damage.

## Data

Since D&D is a locally (off web) played game, there isn't really much data out there on combat encounters in the game. So, I decided to create my own data set, using the [BattleSim](https://battlesim-zeta.vercel.app/) created by the youtuber [Trekiros](https://www.youtube.com/@trekiros)

The following question might be "Since you are predicting the results of a simulated combat, there is a margin of error on top of the original margin of error of the simulator, so how can you be sure that the results are accurate?". Well, I can't, but I used the simulator a couple of times for real playercontrolled encounters, and the results were pretty accurate, so I'm confident that the results are accurate enough.

And to minimize the margin of error even further, I had to take some liberties with the data.

### Data collection

The data was collected by running the simulator 100.000. Every time I generated a new random party, with 3-5 PCs, levels 1-5, and 1-5 monsters, CR 1/8-13. I did that way because most parties are between 3 to 5 players, and in 5e, when you get past level 5 abilities start to get a bit to crazy/unpredictable, so I decided to limit the data to level 5. And the same goes for the monsters, most of the time you will be fighting 1-5 monsters, and to avoid the case of trowing 5 liches against a party of 3 level PCs, I limited the CR to 13, with shoukd be the maximum a oarty of 5 level 5 PCs would encounter.

### Dataset

The dataset is a csv file with 100.000 rows and _ columns, with the following columns:

| Column name | What it represents |
|-------------|--------------------|
|$p_i$ _class|The class of the respective player, $1\le i\le 5$ (``string``)|
|$p_i$ _hp|The total hitpoints of the respective player, $1\le i\le 5$ (``integer``)|
|$p_i$ _armour_class|The armour class of the respective player, $1\le i\le 5$ (``integer``)|
|$p_i$ _avg_save|The value of the average saving throw of the respective player, $1\le i\le 5$ (``integer``)|
|players_level|The level of the party (``integer``)|
|monster_name|Name of the monster (``string``)|
|monster_ac|The armour class of the monster (``integer``)|
|monster_size|The size of the monster *(T,S,M,L,H,G)* (``string``)|
|monster_type|The type of the monster (``string``)|
|num_of_monsters|Number of monsters in the encounter (``integer``)|
|monster_cr|The value of the monster's Chalenge Rating (``float``)|
|monster_hp|The total hitpoints of the monster (``integer``)|
|difficulty|The difficulty of the encounter (``string``)|

### Inputs/Outputs

Inputs

- Players classes
- Players levels
- Players hitpoints
- Players armour class
- Players average saving throw
- Number of monsters
- Monster CR
- Monster hitpoints
- Monster armour class
- Monster size
- Monster type

Outputs

- Encounter difficulty class

## Models

The models used were two XGBoost models, one regressor and one classifier. The regressor was used to predict the difficulty of the encounter, and the classifier was used to classify the encounter as a TPK or a victory for the players.

### Regressor

The regressor was trained, several times, tuning hyperparameters and scaling the data, ultimately, the best model was made with no feature scaling, and the following hyperparameters:

- ```n_estimators```:
- ```max_depth```:
- ```learning_rate```:
- ```gamma```:
- ```min_child_weight```:
- ```colsample_bytree```:
- ```scale_pos_weight```:
  
### Classifier

The classifier was also trained several times, tuning hyperparameters and scaling the data, ultimately, the best model was made with no feature scaling, and the following hyperparameters:

- ```n_estimators```: 200,
- ```max_depth```: 6,
- ```learning_rate```: 0.2,
- ```gamma```: 0.2,
- ```min_child_weight```: 3,
- ```colsample_bytree```: 0.6000000000000001
- ```scale_pos_weight```: 2.03

## Features

- Data Collection using Web Scraping
- Machine Learning model to fit the data
- API implementation
- Front-end interaction

## Installation

1. Clone the repo

    ```sh
    git clone https://github.com/pedrogjmesquita/5e_encounter_predictor.git
    ```

2. Creating a virtual environment

    ```sh
    python - venv venv
    ```

3. Activating the virtual environment

    ```sh
    .\venv\Scripts\activate
    ```

4. Installing the requirements

    ```sh
    pip install -r requirements.txt
    ```

## Usage

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pedro Mesquita - [pedro.gjmesquita@gmail.com](mailto:pedro.gjmesquita@gmail.com)

Project Link: [https://github.com/pedrogjmesquita/5e_encounter_predictor](https://github.com/pedrogjmesquita/5e_encounter_predictor)
