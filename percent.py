import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    percent = []
    days = []

    with open(data_path) as f :
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            percent.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
        
    return{"x" : percent, "y" : days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation is:-",correlation[0][1])

def plotFigure(data_path):
    with open("percent.csv") as r:
        df = csv.DictReader(r)
        fig = px.scatter(df,x = "Marks In Percentage",y="Days Present")
        fig.show()

def setup():
    data_path = "percent.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()    
