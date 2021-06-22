import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    array1=[]
    array2=[]
    with open(data_path) as file:
        reader=csv.DictReader(file)
        for i in reader:
            array1.append(float(i["Temperature"]))
            array2.append(float(i["Ice-cream Sales( ₹ )"]))
    return{"x": array1, "y": array2}
def findCorelation(datasource):
    Corelation=np.corrcoef(datasource["x"],datasource["y"])    
    print("correlation is:",Corelation[0,1])

def setup():
    data_path="Data1.csv"
    datasource=getdatasource(data_path)
    findCorelation(datasource)

setup()    

