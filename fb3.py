import json
import pandas as pd
import nltk
import matplotlib.pyplot as plt
%matplotlib inline  
a=pd.read_json('D:/comment_data.json')
a
a["comment"][0]
testing=a["comment"][0:5]
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()
summary = {"positive":0,"neutral":0,"negative":0}
for i in testing:
    word=i.split()
    for j in word:
        ss=sid.polarity_scores(j)
        if ss["compound"] == 0.0: 
            summary["neutral"] +=1
        elif ss["compound"] > 0.0:
            summary["positive"] +=1
        else:
            summary["negative"] +=1
    print("sentence ends")
print(summary)
x, y = zip(*summary)
plt.pie(x,y, colors=["red","blue","green"],
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()

