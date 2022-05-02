import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("data.csv")
data=df["average"].tolist()
mean=statistics.mean(data)
#fig=ff.create_distplot([data],["average"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
#fig.show()

#code to finD meAN OF COUNTER(100) SAMPLE INDEX 

def randomsetofmean():
    dataset=[]
    for i in range(0,100):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


#caaling function 1000 times
meanlist=[]
for i in range(0,1000):
    r=randomsetofmean()
    meanlist.append(r)

#now creating graph after  this sample data 
mean1=statistics.mean(meanlist)
fig = ff.create_distplot([meanlist], ["average"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,15],mode="lines",name="mean"))
fig.show()
