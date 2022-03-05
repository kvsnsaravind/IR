# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
#import urllib.request 
import urllib
from urllib.request import urlopen
from urllib.parse import quote
import os
os.mkdir('BM25')
f= open('test-queries.txt',encoding='utf-8')
file_no=1
for j in f:
    q_id,i=j.split(' ',1)
    j=j.replace(":","\:")
    query=quote(j)


# change the url according to your own corename and query
    inurl = 'http://3.15.1.148:8983/solr/IRF21_p3_BM25/select?defType=dismax&fl=id%20score&q.op=OR&q=*'+query+'*&qf=text_en%20text_ru%20text_de%20tweet_urls%20tweet_hashtags&rows=20'
    outfn = str(file_no)+'.txt'
    file_no+=1


    # change query id and IRModel name accordingly
    qid = q_id
    IRModel='bm25' #either bm25 or vsm
    outf = open('BM25/'+outfn, 'w')
    data = urlopen(inurl)
    # if you're using python 3, you should use
    # data = urllib.request.urlopen(inurl)

    docs = json.load(data)['response']['docs']
    # the ranking should start from 1 and increase
    rank = 1
    for doc in docs:
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()

