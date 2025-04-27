# 📈 Stock Price Prediction Web App

This is a Django-based web application that predicts the **next day's closing stock price** for a company based on historical data using **Linear Regression**.  
The stock data is fetched live from **Yahoo Finance API** using `yfinance`.

---

## 🚀 Features

- Fetches 1 year of historical stock data
- Uses Machine Learning (Linear Regression) for prediction
- Simple and clean web interface (HTML + Django)
- Real-time prediction for any stock symbol (e.g., AAPL, MSFT, TSLA)

---

## 🛠️ Technologies Used

- Python 3.10
- Django 5.2
- Pandas
- Scikit-learn
- Yahoo Finance API (`yfinance`)
- HTML & Bootstrap (optional for styling)

---

## 📂 Project Structure

```plaintext
stockpredictor_ready/
├── manage.py
├── stockpredictor/
│   ├── settings.py
│   ├── urls.py
├── prediction/
│   ├── views.py
│   ├── stock_predictor.py
│   ├── templates/
│       └── home.html

**How to Run Locally**
_
1. Clone the repository:

bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install the required libraries:

bash

pip install django yfinance pandas scikit-learn

3. Apply migrations:

bash

python manage.py migrate

4. Run the development server:

bash

python manage.py runserver

5. Open your browser and visit:

cpp

http://127.0.0.1:8000/

**How It Works**
User enters a stock symbol (e.g., AAPL for Apple Inc.)

The app fetches last 1 year of stock data from Yahoo Finance

Linear Regression model is trained on Open, High, Low, Close, Volume features

Predicts the next day's closing price

Displays the prediction on the webpage

Author
Payal Thakur
