import json
from django.shortcuts import render
import MySQLdb
from django.http import JsonResponse
# Create your views here.
import pandas as pd
def weather(request):
    data = pd.read_csv('weather.csv')
    new_data = []
    for i in range(len(data)):
        new_data.append(str(data.loc[i]).split("\n")[0].split(" ")[-2:])
    new_df = pd.DataFrame(new_data,columns=["지역","온도"])
    labels = new_df['지역'].tolist()
    temperature = new_df['온도'].astype(float).tolist()
    # print(labels)
    # print(temperature)
    datasets = [
        {
            'label': 'temperature',
            'data': temperature,
            'backgroundColor': 'rgba(255, 99, 132, 0.5)'
        }
    ]
    weather_data = {
        'labels': labels,
        'datasets': datasets
    }

    return render(request, 'weather/weather.html', {'weather_data': json.dumps(weather_data)})

    

    



