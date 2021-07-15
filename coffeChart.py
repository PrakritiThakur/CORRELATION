import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleepHours = []

    with open(data_path)as f :
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleepHours.append(float(row["sleep in hours"]))
    
    return{"x" : coffee,"y":sleepHours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"])
    print("Correlation is :-",correlation[0][1])

def plotFigure(data_path):
    with open('coffee.csv')as f :
        df = csv.DictReader(f)
        fig = px.scatter(df,x = "Coffee in ml",y = "sleep in hours")
        fig.show()

def setup():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    plotFigure(data_path)
    findCorrelation(datasource)

setup()