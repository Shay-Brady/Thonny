import pandas as pd

df = pd.read_csv('summer.csv')

countries=df["Country"]
count={}
for item in countries:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
        

maximum = max(count, key=count.get)
print("Maximum value:",maximum)





