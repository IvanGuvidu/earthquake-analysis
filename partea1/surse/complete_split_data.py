import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def complete_data_and_split(df):
    df_encoded = df.copy()
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
    })
    scaler = MinMaxScaler()
    coloane_numerice = ['longitudine', 'latitudine', 'adancime epicentru', 'replici', 'magnitudine ultimul']
    df_encoded[coloane_numerice] = scaler.fit_transform(df_encoded[coloane_numerice])
    return df_encoded