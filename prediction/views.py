from django.shortcuts import render
from . import stock_predictor

def home(request):
    prediction = None
    if request.method == 'POST':
        symbol = request.POST['symbol']
        prediction = stock_predictor.predict_stock(symbol)

    return render(request, 'home.html', {'prediction': prediction})
