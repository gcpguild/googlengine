"""
Google Engine Search by SerpAPI 
Python : Create the Google search JSON.

Project contact: Google Cloud Search API, Kyndryl
Email: Ramamurthy.valavandan@kyndryl.com
Python API for Google Search Engine
Use Case: Creating the Temples List, Description of Temple, Co-ordinates, Distances from major cities in India.

Purpose : After connecting to Google Search Engine API the JSON is generated
This program is used to connect Google Search API (SerpAPI) 
Download the searched information which is saved in the JSON file based on the Google Search Engine.
Create the necessary folders in local and download and save JSON for locally parse the search key.
---------------------------------------------------------------------------------------------------
SerpAPI Sponsorship
Google Engine is sponsored by SerpApi. SerApi has sponsored 40,000 credits for Google search
with the API Key for scraping Google and other search engines.

On behalf of Google Engine, researchers, we express our gratitude to SerpAPI LLC, for provisioning
their sponsorship SerpAPI's sponsorship has helped us make our research and social work contribution 
for speaking out greater audience.
With the advent of SerpAPI, Google Engine has addressed our research work on Temples in India 
with the experience of a blazingly fast, super easy to use, and data-rich API in 
Google Cloud Platform Search Engine on Big Query for Research in Google Cloud Engine. 
With SerpAPI, Google Engine will be helping the student community on projects.

About SerpApi
-------------
SERP API is a real-time API to access Google search results. 
It solves the issues of having to rent proxies, solving captchas, and JSON parsing.

Design and developed by :
-------------------------
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Google Engine @ SerApi, LLC.

Download from Git Hub

https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py

How to use
------------
python searchapiexcelfilter.py 

Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
Email: ramamurthy.valavandan@kyndryl.com
GCP Contact: gcpguild@gmail.com
Date: June 21, 2022.
Contributors: 22 key members from Google Cloud Search API.

For SerpAPI Key request, please write an email request with an email subject of 'request for SerpApi Key'

Email: ramamurthy.valavandan@kyndryl.com
"""
#-----------------------------------------------------#-----------------------------------------------------
githubserpaijson = "https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py"

serpapitemplestutindiagoogle = ['62b115ac2e7d6bafc2e13610.json']

import json, re, csv, os, unicodedata, requests, string
import ijson
from bs4 import BeautifulSoup
from pathlib import Path
from six.moves.urllib.request import urlopen

import pandas as pd

import urllib.request

import numpy as np

from requests import request
from urllib.error import URLError

from itertools import filterfalse

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

basepath = "C:"
codepath="google"
function = "serpapi"
N="\\"
namefile = "indias"
max_gs = 10 # maximum number of google search in href or urls
#-----------------------------------------------------
indiatempledatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))


datadirgoo = ("{}_{}".format(namefile.capitalize(),"googlengine_temple_States_and_UTs"))

googledataindiastutdir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))

cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)

indiastautfile = ("{}{}{}".format(googledataindiastutdir,N,"Ind_googlengine_states_ut_master.csv"))
#-----------------------------------------------------
path = Path(indiastautfile)


if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    
else:
    pi="\'Data of States and UTs is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    pi="\'Execute myindiagenStatesandUTdata.py First !\' :"
    statesutpy = "Get from Git Hub"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Download :' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/myindiagenStatesandUTdata.py"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Save myindiagenStatesandUTdata.py \' :"
    statesutpy = "in c:\python\indias"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Document :\' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/Python%20Lab%20India_states_UT.docx"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    exit(1)
#-----------------------------------------------------
templemanog = []
imginlinepslist = []
serpapilinks = []
organic_results = []
related_searches = []
inline_people_also_search_for = []
related_questions = []
related_results = []

cleantemples = []

#-----------------------------------------------------
def gematerials(data,di):

  
    li = ''
    li = len(data[di])
  
    if (di == "organic_results"):
        for i in range(0,li):
            gor = ''
            gor = data[di][i]['snippet']
            organic_results.append(gor)
            templemanog.append(gor)
            
            golink = data[di][i]['link']

           
            serpapilinks.append(golink)
       
    if (di == "related_searches"):
        for i in range(0,li):
            gor = data[di][i]
            if (gor):
                gor = data[di][i]['query']
                rsl = data[di][i]['link']
                serpapilinks.append(rsl)
                related_searches.append(gor)
                templemanog.append(gor)
            
    if (di == "inline_people_also_search_for"):
        for i in range(0,li):
            gor = data[di][i]
            if (gor):
                inls = len(data[di][i]["items"])
                
                for n in range(0,inls):
                  
                    goinline = data[di][i]["items"][n]['name']
                    inline_people_also_search_for.append(goinline)
                    templemanog.append(goinline)
                    image = data[di][i]["items"][n]['image']

                    imginlinepslist.append(image)
                  

    if (di == "related_questions"):
     
            for j in range(0,li):
                
                goinlinein = data[di][j]['question']
                
               
                related_questions.append(goinlinein)
                templemanog.append(goinlinein)
    if (di == "pagination"):
        
       serpapilinks.append(data[di]['next'])

       serpapilinks.append(data[di]['other_pages']['2'])
       serpapilinks.append(data[di]['other_pages']['3'])
       serpapilinks.append(data[di]['other_pages']['4'])
       serpapilinks.append(data[di]['other_pages']['5'])
       serpapilinks.append(data[di]['other_pages']['6'])
       serpapilinks.append(data[di]['other_pages']['7'])
       serpapilinks.append(data[di]['other_pages']['8'])
       serpapilinks.append(data[di]['other_pages']['9'])
       serpapilinks.append(data[di]['other_pages']['10'])

    temdat =  []

 
    lt = len(templemanog)
  
    for t in range(0, lt):
     
        tel = templemanog[t]
        if (tel):
         
      
            m = [ x.strip() for x in ''.join(tel).strip('[]').split(',') ]
            if m not in temdat:
                temdat.append(m[0])

            else:
                print("Duplicate is removed", t)
          
    return temdat 

#-----------------------------------------------------
wordcsvpath = ("{}{}{}".format(googledataindiastutdir,N,"word_master.csv"))

wordmfile = Path(wordcsvpath)

if wordmfile.is_file():
    pi="\'Words data : \' :"
    p = ("{} {}".format(pi,wordmfile))
    prt(p)
    
else:
    pi="\'World filter data is missing!\' :"
    p = ("{} {}".format(pi,wordmfile))
    prt(p)
    pi="\'Execute words.py First !\' :"
    exit(1)

fields = ['List of words']

df_words = pd.read_csv(wordmfile, skipinitialspace=True, usecols=fields)
#-----------------------------------------------------
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)
#-----------------------------------------------------
fv = []

for w in (df_words[fields[0]]):
    
    w = re.sub(r'[^a-zA-Z]','',str(w))
    normals = normalize_caseless(w)
    
    fv.append(normals)

#-----------------------------------------------------
templesgooglengine = []

def referal(serpapisearchedjsontempledata):
    
    with open(serpapisearchedjsontempledata) as fh:
        data = json.load(fh)
       
        for d in (data):

            try: 
                temdat = gematerials(data = data, di = d)
            except KeyError: pass  
    if (temdat):
        for t in (temdat):
  
            templeword = [re.sub(r'[^a-zA-Z]+', ' ', k) for k in t.split("\n")]
            mano = ''
            for x in templeword:
                    mano += ' '+ x
            templel = re.findall(r'\S+', str(mano))
        
            manogioo = ''
            for y in templel:
                    manogioo += ' '+ y
                    templewordmano = [re.sub(r'[^a-zA-Z]+', ' ', k) for k in manogioo.split("\S+")]
                   
            templesgooglengine.append(templewordmano)

          
    return templesgooglengine

#-----------------------------------------------------
df = pd.read_csv(indiastautfile, delimiter=',',
on_bad_lines='skip', 
engine="python"
)
#-----------------------------------------------------
def serapitemplesoutfile(st,csvf):

    templesgoogleoutcsv = ''
    templesgoogleoutcsv = ("{}_{}_{}".format(namefile.capitalize(),st,csvf))
    serpapisearchedtempledatastate = ''
    serpapisearchedtempledatastate = ("{}{}{}".format(googledatastunindiadir,N,templesgoogleoutcsv))
    return serpapisearchedtempledatastate

#-----------------------------------------------------
templesget = sorted([list(row) for row in df.values])

sul =  []

cap = []

for t in templesget:


  m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
  
  if m not in sul:
      sul.append(m[0])
      cap.append(m[1])

  else:
        print("Duplicate is removed", t)

csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
    capital = re.sub(patternspace, '-', cap[cc])
    googledatastunindiadir = ''
    googledatastunindiadir = ("{}{}{}".format(googledataindiastutdir,N,statename))
    
    cre_directory = Path(googledatastunindiadir)
    cre_directory.mkdir(parents=True, exist_ok=True)
    inputfile_google_json = ''
    inputfile_google_json = serpapitemplestutindiagoogle[0]
       
    sepapi_json = ("{}_{}_{}".format(namefile.capitalize(),statename,inputfile_google_json))

    indiastautjsonfile = ''
    indiastautjsonfile = ("{}{}{}".format(googledatastunindiadir,N,sepapi_json))

    indiafilepushtxt = ''
    indiafilepushtxt = ("{}_{}_{}".format(namefile.capitalize(),statename,inputfile_google_json))
    serpapisearchedjsontempledata = ''
    serpapisearchedjsontempledata = ("{}{}{}".format(cre_directory,N,indiafilepushtxt))

    templesserpapifilterdata = serapitemplesoutfile(st = statename,csvf ="Temples_Google_SerpApi.csv")
    GooglePaginationsSerplinks = serapitemplesoutfile(st = statename,csvf ="Google_Paginations_Links_SerpApi.csv")
    sf = Path(serpapisearchedjsontempledata)

    if sf.is_file():
        pi= ("{}{}".format("State or UT name : ", statename))
        p = ("{}".format(pi))
        prt(p)

        pi="\'Google data of temples in state or UT for :\' :"
        p = ("{} {}".format(pi,statename))
        prt(p)
        p = ("{}".format(serpapisearchedjsontempledata))
        prt(p)

        readdata = referal(serpapisearchedjsontempledata)
        if(readdata):
          
            tegoog = []
            tl = len(templesgooglengine)
            for g in range(0,tl):
                tg = templesgooglengine[g]
           
                ma = ''
                for m in (tg):
                    ma += ' '+ m
                m = re.findall(r'\S+', str(ma))
               
                for e in range(0,len(m)):
                    tgl = (m[e]).lower()
                    tn = normalize_caseless(tgl)
                    if tn not in tegoog:
                  
                        tegoog.append(tn)
            csl = []
            for sc in [capital, statename]:
                i = normalize_caseless(sc)
                i = re.sub('-',' ',i)
                csl.append(i)
              
                
    else:
        pi="\'The JSON is missing :\' :"
        p = ("{} {}".format(pi,statename))
        prt(p)
        pi ="Perform Python to download JSON.. "
        p = ("{} {}".format(pi, githubserpaijson))
        prt(p)
        exit(1)
#----------------------------------------------------- 
l1 = tegoog
l2 = set(fv)


filt = list(filterfalse(l2.__contains__, l1))

cleanlinksout = []

for l in range(0,len(serpapilinks)):

    cleanlinksout.append(serpapilinks[l])

#-----------------------------------------------------
tf = pd.DataFrame(filt)

mudit = ['List of temples' ]
mode = 'w' if mudit else 'a'

tf.to_csv(templesserpapifilterdata, encoding='utf-8', mode=mode, header=mudit)

templescsvfile = Path(templesserpapifilterdata)

if  templescsvfile.is_file():
    pi="\'SerpApi Google filtered temples data : \' :"
    p = ("{} {}".format(pi,templescsvfile))
    prt(p)

#-----------------------------------------------------
tfl = pd.DataFrame(cleanlinksout)

mudil =  ['Google SerApi Links']
model = 'w' if mudil else 'a'

tfl.to_csv(GooglePaginationsSerplinks, encoding='utf-8', mode=model, header=mudil)

templescsvgooglefile = Path(GooglePaginationsSerplinks)

if  templescsvgooglefile.is_file():
    pi="\'SerpApi Google Links data : \' :"
    p = ("{} {}".format(pi,templescsvgooglefile))
    prt(p)
#-----------------------------------------------------