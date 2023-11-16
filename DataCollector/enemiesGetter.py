from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import accept_cookies_button
import pandas as pd


# create a new Chrome browser instance
driver = webdriver.Edge()

# navigate to Google search
driver.get("https://battlesim-zeta.vercel.app/")
sleep(3)

# accept cookies
driver.find_element(By.XPATH, accept_cookies_button).click()

driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div[1]/button').click()
table = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div[2]/div/div[2]/div/div')
enemies = table.text.split("\n")[2:-1]

driver.quit()

enemy_list = []
cr_list = []
for i in range(len(enemies)//3):
    enemy_list.append(enemies[3*i])
    cr_list.append(enemies[3*i+2])

df = pd.DataFrame({'Enemy': enemy_list, 'CR': cr_list})

df.to_csv('Data\enemies.csv', index=False)