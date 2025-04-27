import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import datetime

def predict_stock(symbol):
    # Get historical stock data (last 1 year)
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365)
    data = yf.download(symbol, start=start, end=end)

    if data.empty:
        return "No data found for this symbol."

    # Feature selection
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data['Target'] = data['Close'].shift(-1)
    data.dropna(inplace=True)

    # Inputs and output
    X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = data['Target']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the next day price
    latest_data = X.tail(1)
    predicted_price = model.predict(latest_data)[0]

    return round(predicted_price, 2)
