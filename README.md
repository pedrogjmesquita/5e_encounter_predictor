# 5e Combat Predictor

This is a D&D 5th Edition Combat Ecounter predictor using Machine Learning algorithms. The goal is to predict the outcome of a combat encounter based on the stats of the players and the monsters, classifying the encounter in cattegories such as "Very Easy", "Easy","Medium", "Hard", "Very Hard" and "TPK" following a set of criteria defined by me.

## Table of dificulty

| Difficulty | Threshold |
|------------|-----------|
|Very Easy   | All party members with more than half their life left |
|Easy        | At least 2 party members with more than half their life left, and none unconscious |
|Medium      | At least 1 party member with more than half their life left, and none unconscious |
|Hard        | At least 1 party member with more than half their life left, and at least 1 unconscious |
|Very Hard   | At least 2 party members unconscious, and at least 1 conscious |
|TPK         | All party members unconscious |

## Data

Since D&D is a locally (off web) played game, there isn't really much data out there on combat encounters in the game. So, I decided to create my own data set, using the [BattleSim](#https://battlesim-zeta.vercel.app/) created by the youtuber [Trekiros](https://www.youtube.com/@trekiros).<br><br>
The following question might be "Since you are predicting the results of a simulated combat, there is a margin of error on top of the original margin of error of the simulator, so how can you be sure that the results are accurate?". Well, I can't, but I used the simulator a couple of times for real playercontrolled encounters, and the results were pretty accurate, so I'm confident that the results are accurate enough.<br><br>
And to minimize the margin of error even further, I had to take some liberties with the data.

### Data collection

The data was collected by running the simulator 100.000. Every time I generated a new random party, with 3-5 PCs, levels 1-5, and 1-5 monsters, CR 1/8-13. I did that way because most parties are between 3 to 5 players, and in 5e, when you get past level 5 abilities start to get a bit to crazy/unpredictable, so I decided to limit the data to level 5. And the same goes for the monsters, most of the time you will be fighting 1-5 monsters, and to avoid the case of trowing 5 liches against a party of 3 level PCs, I limited the CR to 13, with shoukd be the maximum a oarty of 5 level 5 PCs would encounter.

### Data cleaning


### Dataset

The dataset is a csv file with 100.000 rows and _ columns, with the following columns:
<br>
| Column name | What it represents |
|-------------|--------------------|
|$P_i$ _class|The class of the respective player, $1\le i\le 5$ (``string``)|
|$P_i$ _hp|The total hitpoints of the respective player, $1\le i\le 5$ (``integer``)|
|$P_i$ _armour_class|The armour class of the respective player, $1\le i\le 5$ (``integer``)|
|$P_i$ _avg_save|The value of the average saving throw of the respective player, $1\le i\le 5$ (``integer``)|
|Players_level|The level of the party (``integer``)|
|Monster_name|Name of the monster (``string``)|
|N_monsters|Number of monsters in the encounter (``integer``)|
|Monster_cr_rating|The value of the monster's Chalenge Rating (``float``)|
|Monster_hp|The total hitpoints of the monster (``integer``)|
|$P_i$ _remaining_hp|The total hitpoints remained of the respective player after the encounter, $1\le i\le 5$ (``integer``)|
|Encounter_difficulty|The difficulty of the encounter (``string``)|

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

Outputs
- Encounter difficulty class

## Features

- Data Collection using Web Scraping
- Machine Learning model to fit the data
- API implementation
- Front-end interaction

## Installation

1. Clone the repo
    ```sh
    git clone https://github.com/your_username_/Project-Name.git
    ```
2. Install packages
    ```sh
    pip install pandas==2.0.3
    ```
    ```sh
    pip install selenium==4.14.0
    ```

## Usage



## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pedro Mesquita - [pedro.gjmesquita@gmail.com]()

Project Link: [https://github.com/your_username/repo_name](https://github.com/pedrogjmesquita/5e_encounter_predictor)
