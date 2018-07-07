from flask import Flask, render_template
import requests 
import requests 
import pandas as pd
import os, sys
import sqlite3
import json
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
app=Flask(__name__)
@app.route('/result')
def result():
	dict={'phy':50,'che':60,'mat':70}
	return render_template('result.html',result=dict)
@app.route('/comments')
def comments():
	return render_template('pp.html')
@app.route('/fb')
def fb():
	fb_pageid = "1630198273694692"#this is the facebook pade id which has the post
	fb_postid = "1630216223692897"#this is the facebook post id which is page mmentioned before
	commentlst = []#for storing and appending 
	datelst = []
	url = "https://graph.facebook.com/v3.0/"+ fb_pageid +"_"+ fb_postid +"/comments?limit=100&access_token="+"EAAF3aT1tbSwBAFEM6zCjPmabxyL7wG6Tzhul5RjURWaXWexsqOJU62HfxQZBsdSMBAJzPIwIw1kHKLeIkCsPevGekTHG258NRotb9ZBDpDagZBhBSgwrJhdWOnaXkQoncRa4gtjKBanPHag8rZCSKKoIXF1GdDF0VNunZBieSuQZDZD"
	while(True):
	    posts = requests.get(url)#requests http requests
	    posts_json = posts.json()
	    for x1 in posts_json['data']:#looping in request data,here each comments are processed
	        commentlst.append(x1.get('message').encode('utf-8').strip())#appending comments data from request
	        datelst.append(x1.get('created_time'))#appending time in a format
	    next_page = ""
	    try:
	        next_page = posts_json['paging']['next']#page contains limit so rolling through pages
	        url = next_page
	    except:
	        break
	    if not next_page: 
	        break
	    print ("Count: %s,  Next Page: %s" % ( len(commentlst), url))
	print ("\nGenerating JSON File")#json file is generated in the working directory
	df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
	df['dates'] = pd.to_datetime(df['dates'])
	df['day_of_week'] = df['dates'].dt.weekday_name
	df['year'] = df['dates'].dt.year
	df['month'] = df['dates'].dt.month
	df['count'] = 1 
	df.to_json('comment_data.json')
	return("json generated")
@app.route('/analyse')
def analyse():
	a=pd.read_json('comment_data.json')
	testing=a["comment"]
	sid=SentimentIntensityAnalyzer()
	summary={"positive":0,"neutral":0,"negative":0}
	for i in testing:
		tagged_sentence=nltk.tag.pos_tag(i.split())
		edited_sentence=[word for word,tag in tagged_sentence if tag!='NNP' and tag!='NNPs']
		end=' '.join(edited_sentence)
		ss=sid.polarity_scores(end)
		if ss['compound']==0.0:
			summary["neutral"]+=1
		elif ss["compound"]>0.0:
			summary['positive']+=1
		else:
			summary['negative']+=1
	values=[ k for k in summary.values() ]
	labels=["Positive","Neutral","negative"]
	#values=[10,9,8,7,6,4,7,8]
	colors=["#F7464A","#46BFBD","#FDB45C"]
	return render_template( 'graph.html',set=zip(values,colors))
if __name__=='__main__':
	app.run(debug=True)