import requests 
import requests 
import pandas as pd
import os, sys
fb_pageid = "162105521324822"
fb_postid = "162537737948267"
commentlst = []
datelst = []
url = "https://graph.facebook.com/v3.0/"+ fb_pageid +"_"+ fb_postid +"/comments?limit=100&access_token="+"EAAF3aT1tbSwBAJdaji21qIdFaK62AxoUaL4ELvvUjBsfKKdHAWPH2oAF1lzBTLJPw76bysmI6wLqVWNzRVhXPDdIuXrZChU42wv1NuAFMc1aFCAK9kj86KH8WJMZBnkhwZBEZBOrjiObAkA3xhvTPLyvZBVFEZA2jiLZBHKVZBkH6QZDZD"
while(True):
    posts = requests.get(url)
    posts_json = posts.json()
    for x1 in posts_json['data']:
        commentlst.append(x1.get('message').encode('utf-8').strip())
        datelst.append(x1.get('created_time'))
    next_page = ""
    try:
        next_page = posts_json['paging']['next']
        url = next_page
    except:
        break
    if not next_page: break
    print "Count: %s,  Next Page: %s" % ( len(commentlst), url)

print "\nGenerating JSON File"

df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
df['dates'] = pd.to_datetime(df['dates'])
df['day_of_week'] = df['dates'].dt.weekday_name
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['count'] = 1 

df.to_json('comment_data.json')