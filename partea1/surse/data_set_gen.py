import pandas as pd
import numpy as np
import random

def data_set_gen():
    np.random.seed(0) # pentru a avea consistente datele, pentru full random, scoatem aceasta linie
    random.seed(0)
    n = 1000
    zi = np.random.randint(1, 30, n)
    latitudine = np.random.uniform(0, 90, n)
    longitudine = np.random.uniform(0, 180, n)
    adancime_epicentru = np.random.uniform(50, 100, n)
    tip_placa = np.random.choice(['convergenta', 'divergenta', 'transformare'], n, p = [0.4, 0.2, 0.4])
    replici = np.random.randint(1, 10, n)
    magnitudine_ultimul = np.random.uniform(1.5, 9, n)
    magnitudine = np.full(n, 2.0)
    for i in range(n):
        if tip_placa[i] == 'convergenta':
            magnitudine[i] += np.random.uniform(0, 1)
        elif tip_placa[i] == 'divergenta':
            magnitudine[i] += np.random.uniform(1, 2)
        else:
            magnitudine[i] += np.random.uniform(2, 3)
    magnitudine -= (magnitudine_ultimul - 2) * 0.2
    magnitudine += 0.1 * replici
    magnitudine += 0.025 * adancime_epicentru
    for i in range(n):
        if magnitudine[i] < 2.0:
            magnitudine[i] = 2.0
        if magnitudine[i] > 9.0:
            magnitudine[i] = 9.0 
    df = pd.DataFrame({
        'zi' : zi,
        'longitudine': longitudine,
        'latitudine': latitudine,
        'adancime epicentru': adancime_epicentru,
        'tip placa': tip_placa,
        'replici' : replici,
        'magnitudine ultimul' : magnitudine_ultimul.round(1),
        'magnitudine' : magnitudine.round(1),
    })
    for col in df.columns:
        if col == 'magntidude':
            continue
        x = random.randint(0, 100)
        for i in range(1, x + 1): # alteram x%% (la mie) date
            j = random.randint(0, n - 1)
            df.loc[j, col] = np.nan
    print(df.describe())
    df.to_csv('../date/cutremure.csv', index = False)
    return df