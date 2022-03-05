from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib
from urllib.request import urlopen
from urllib.parse import quote
import os
import nltk
nltk.download('vader_lexicon')

import warnings
warnings.filterwarnings('ignore')
#from .forms import UserForm

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

def analyze_tweet(tweet):
    analysis = {}
    ss = sid.polarity_scores(tweet)
    for k in sorted(ss):
        analysis[str(k)] = float(ss[k])
    return analysis

def home(request):
	return render(request,'accounts/dashboard.html')
def overview(request):
	return render(request,'accounts/overview.html')
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		
		dropdown=request.POST['dropdown']
		print(dropdown)
		searched=searched.replace(":","\:")
		searched=quote(searched)
		#inurl = 'http://ec2-18-189-7-125.us-east-2.compute.amazonaws.com:8983/solr/IRF21_Final_01/select?defType=dismax&df=text_en%20text_hi%20text_es&q.op=OR&q=*'+searched+'*&qf=text_en%20text_hi%20text_es&sort=score%20desc&wt=json&rows=200'
		inurl = 'http://ec2-13-59-10-179.us-east-2.compute.amazonaws.com:8983/solr/IRF21_Final_01/query?q=country:' +dropdown+ '%20and%20tweet_text:' +searched+ '&q.op=OR&fl=id%2Csentiment%2Ccountry%2Ctweet_text%2Ctweet_lang%2Cuser_name%2Cscreen_name%2Creply_text&rows=20&wt=json'
		data = urlopen(inurl)

		data=json.load(data)['response']['docs']
		
		
			
		return render(request,'accounts/search.html',
		{'searched':searched,'data':data})

	else:
		return render(request,'accounts/search.html')

# def filter(request):
# 	if request.method == "POST":
# 		filter=request.POST['filter']
# 		print(filter)
# 		filter=filter.replace(":","\:")
# 		filter=quote(filter)
# 		#inurl = 'http://ec2-18-189-7-125.us-east-2.compute.amazonaws.com:8983/solr/IRF21_Final_01/select?defType=dismax&df=text_en%20text_hi%20text_es&q.op=OR&q=*'+searched+'*&qf=text_en%20text_hi%20text_es&sort=score%20desc&wt=json&rows=200'
# 		inurl = 'http://ec2-18-189-7-125.us-east-2.compute.amazonaws.com:8983/solr/IRF21_Final_01/query?q=country:' +dropdown+ '%20and%20tweet_text:' +searched+ '&q.op=OR&fl=id%2Csentiment%2Ccountry%2Ctweet_text%2Ctweet_lang&rows=20&wt=json'

# 		data = urlopen(inurl)

# 		data=json.load(data)['response']['docs']
		
		
			
# 		return render(request,'accounts/search.html',
# 		{'filter':filter,'data':data})

# 	else:
# 		return render(request,'accounts/searchr.html')
