import plotly.express as px
import csv

with open("Data4.csv") as files:
    df= csv.DictReader(files)
    fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()