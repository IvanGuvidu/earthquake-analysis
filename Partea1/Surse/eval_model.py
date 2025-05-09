from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def eval_model():
    train = pd.read_csv('../date/train.csv')
    y_train = pd.read_csv('../date/y_train.csv').values.ravel()
    test = pd.read_csv('../date/test.csv')
    y_test = pd.read_csv('../date/y_test.csv').values.ravel()
    model = LinearRegression()
    model.fit(train, y_train)
    y_pred = model.predict(test)
    mse = mean_squared_error(y_pred, y_test)
    print(f"Mean squared error: {mse:.2f}")
    plt.scatter(y_test, y_pred)
    plt.title('Predictii vs Valori reale')
    plt.savefig('../date/grafice/predictii.png')
    plt.close()
