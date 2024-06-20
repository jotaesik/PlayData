import json
from django.shortcuts import render
import MySQLdb
from django.http import JsonResponse
# Create your views here.

def chart(request):

    db_config = {
    "host" : "IP",
    "user" : "user",
    "password" : "password",
    "database" : "encore_web"
    }
    con = MySQLdb.connect(**db_config)
    cur = con.cursor()
    cur.execute("select * from result")
    data = cur.fetchall()
    cur.close()
    con.close()

    labels    = [x[0] for x in data]
    Cancelled = [x[1] for x in data]
    Divered   = [x[2] for x in data]
    Air       = [x[3] for x in data]

    datasets = [
        {'label' : 'Cancelled','data': Cancelled,'backgroundColor': 'rgba(255,99,132,0.5)'},
        {'label' : 'Divered','data': Divered,'backgroundColor': 'rgba(54,160,235,0.5)'},
        {'label' : 'Air','data': Air,'backgroundColor': 'rgba(75,199,192,0.5)'},

    ]

    chart_data = {
        'labels' : labels,
        'datasets' : datasets
    }

    return render(request, 'mychart/chart.html', {'chart_data': json.dumps(chart_data)})

