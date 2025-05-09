import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def complete_data_and_split(df):
    for col in df.columns:
        if col == 'magnitudine':
            continue
        x = df[col].isna().sum()
        y = x
        x = x / len(df[col]) * 100
        print(f"Pe coloana {col} lipsesc {x:.2f}% date ({y} valori)")
    df_encoded = df.copy()
    df_encoded = df_encoded.sample(frac = 1, random_state = 42).reset_index(drop = True)
    df_encoded['zi'].fillna(df_encoded['zi'].mean(), inplace=True)
    df_encoded['longitudine'].fillna(df_encoded['longitudine'].mean(), inplace=True)
    df_encoded['latitudine'].fillna(df_encoded['latitudine'].mean(), inplace=True)
    df_encoded['adancime epicentru'].fillna(df_encoded['adancime epicentru'].mean(), inplace=True)
    df_encoded['tip placa'].fillna(df_encoded['tip placa'].mode()[0], inplace=True)
    df_encoded['replici'].fillna(df_encoded['replici'].mode()[0], inplace=True)
    df_encoded['magnitudine ultimul'].fillna(df_encoded['magnitudine ultimul'].mean(), inplace=True)
    df_encoded['magnitudine'].fillna(df_encoded['magnitudine'].mean(), inplace=True)
    df_encoded['tip placa'].replace({
        'convergenta': 0,
        'divergenta': 1,
        'transformare': 2,
    }, inplace=True)
    scaler = MinMaxScaler()
    coloane_numerice = ['longitudine', 'latitudine', 'adancime epicentru', 'replici', 'magnitudine ultimul']
    df_encoded[coloane_numerice] = scaler.fit_transform(df_encoded[coloane_numerice])
    X = df_encoded.drop(columns = ['magnitudine'], axis = 1)
    y = df_encoded['magnitudine']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    X_train.to_csv('../date/train.csv', index = False)
    X_test.to_csv('../date/test.csv', index = False)
    y_train.to_csv('../date/y_train.csv', index = False)
    y_test.to_csv('../date/y_test.csv', index = False)
