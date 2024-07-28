from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

import yfinance

#from rest_framework.response import Response
#from rest_framework.decorators import api_view


# Create your views here.
#@api_view(['GET'])
#def getData(request):
#return Response()

def hello(request):
    return HttpResponse('Hello!')

def getData(request):
    request_ticker: str = request.GET.get('ticker')
    period: str = request.GET.get('p')

    possibleVals = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

    if request_ticker == None: 
        return HttpResponse('No ticker provided!')
    
    if period not in possibleVals:
        period = "5y"

    ticker = yfinance.Ticker(request_ticker)
    history_df = ticker.history(period=period)


    history_json = history_df.to_json()

    history_dict = json.loads(history_json)
    return JsonResponse(history_dict, safe=False)

def getGraph(request):
    request_ticker: str = request.GET.get('ticker')
    period: str = request.GET.get('p')

    possibleVals = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

    if request_ticker == None: 
        return HttpResponse('No ticker provided!')
    
    if period not in possibleVals:
        period = "5y"
    

    ticker = yfinance.Ticker(request_ticker)
    history_df = ticker.history(period=period)
    history_df.plot(y="Close")

    # Save the plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the buffer in base64 and decode to a string
    image_png = buffer.getvalue()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    buffer.close()

    return render(request, 'graph.html', {'graphic': graphic})
