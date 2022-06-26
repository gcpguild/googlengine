"""
Google Engine Search for generate the temple data for the use case.
Use Case: Creating the Temples List, Description of Temple, Co-ordinates, Distances from major cities in India.
Python : Used to create the Google data in CSV format output, input is CSV.

Project contact: GCP Guild moderator, Kyndryl
Email: Ramamurthy.valavandan@kyndryl.com
Design and developed by :
-------------------------
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Nature Labs : Google Engine @ SerApi, LLC.

Download from Git Hub

https://github.com/NATURE-LABS/temples/blob/main/googlenginetempledata.py

How to use
------------
python googlenginetempledata.py

Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
Email: ramamurthy.valavandan@kyndryl.com
GCP Contact: gcpguild@gmail.com
Date: June 25, 2022.
Contributors: 42 key members from GCP Guild.
"""

githubserpaijson = "https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py"



import json, re, csv, os, unicodedata, requests, string

from bs4 import BeautifulSoup
from pathlib import Path
from six.moves.urllib.request import urlopen

import pandas as pd

import urllib.request

import numpy as np

from requests import request
from urllib.error import URLError

from itertools import filterfalse

from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request

from urllib.parse import urlparse


from deepdiff import DeepDiff
from pprint import pprint

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

indiatempledatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))


datadirgoo = ("{}_{}".format(namefile.capitalize(),"googlengine_temple_States_and_UTs"))

googledataindiastutdir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))

cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)

indiastautfile = ("{}{}{}".format(googledataindiastutdir,N,"Ind_googlengine_states_ut_master.csv"))

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
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())
#-----------------------------------------------------
def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)
#-----------------------------------------------------
def common_elemets(a, b):
    ce = [i for i in a if i in b]
    return ce
#-----------------------------------------------------
def searchquery(c,s):
    search = "{} {} {}".format(
    "List of Temples",c, 
     s)
    return searchquery
#-----------------------------------------------------   


def serapitemplesoutfile(st,csvf):

    templesgoogleoutcsv = ''
    templesgoogleoutcsv = ("{}_{}_{}".format(namefile.capitalize(),st,csvf))
    serpapisearchedtempledatastate = ''
    serpapisearchedtempledatastate = ("{}{}{}".format(googledatastunindiadir,N,templesgoogleoutcsv))
    return serpapisearchedtempledatastate
#-----------------------------------------------------
def csvreaddata(inputfile,fields):
    df_csv = pd.read_csv(inputfile, 
    delimiter=',',
    on_bad_lines='skip', 
    engine="python",
    skipinitialspace=True, usecols=[fields])
    
    readdata = sorted([list(row) for row in df_csv.values])
    return readdata
#-----------------------------------------------------
columnname = ['States and Union Territories in India']

stateslist = csvreaddata(indiastautfile,str(columnname[0]))
#------------------word list --------------------
wordcsvpath = ("{}{}{}".format(googledataindiastutdir,N,"word_master.csv"))

wordmfile = Path(wordcsvpath)

fields = ['List of words']

df_words = pd.read_csv(wordmfile, skipinitialspace=True, usecols=fields)

fv = []

for w in (df_words[fields[0]]):
    
    w = re.sub(r'[^a-zA-Z]','',str(w))
    normals = normalize_caseless(w)
    
    fv.append(normals)
#--------------------------------------------------------------------
def getfilters(l1):
    l2 = set(fv)
    filt = list(filterfalse(l2.__contains__, l1))
    return filt
#-------------------------------------------------------------------- 
sul =  []

cap = []

templeslist =  []

for s in stateslist:


  m = [ x.strip() for x in ''.join(s).strip('[]').split(',') ]
  
  if m not in sul:
    sul.append(m[0])
    cap.append(m[1])
   
    st = normalize_caseless(m[0])
    sts = st.split( )
    cp = normalize_caseless(m[1])
    fv.append(st)
    fv.append(cp)
    for s in range(0,len(sts)):
        fv.append(sts[s])
  else:
        print("Duplicate is removed", s)
#--------------------------------
def tagging(gettag):
    dict={
              'templenet.com': 'b',
              'www.nativeplanet.com' : 'h6'
          }
    return dict.get(gettag, 'b')
# ------------------------------------------------------
def googling(url,domainname):
    
    pi="\'Searching website :  \' :"
    p = ("{} {}".format(pi, domainname))
    prt(p)
    request = requests.get(url)
    page = request.text
    soup = BeautifulSoup(page, 'lxml')
    tagslist = []

    for tag in soup.find_all(True):
        t = tag.name
        if t not in (tagslist):
            tagslist.append(t)
           #<b>
    td = []
    gettag = tagging(domainname)
    #print(gettag)
    for x in (tagslist):
        #print(x)
        if (x == gettag):
            #print(x)
            tb = soup.find_all(x)
            #p1 = ("{}{}{}".format('<', x, '>'))
            #p2 = ("{}{}{}".format('</', x ,'>'))
            #mano = re.sub(p1,'', str(tb))
            #mano = re.sub(p2,'', str(mano))
            mano = re.split(r'\s', str(tb))
            #print(mano)
            filt = getfilters(mano)
            if(filt):
                #print(filt)
                #mano = str(ma.split(','))
                #for tg in (tagslist):
                p1 = ("{}{}{}".format('<', x, '>'))
                p2 = ("{}{}{}".format('</', x ,'>'))
                print(p1,p2)
                mano = re.sub(p1,'', str(filt))
                mano = re.sub(p2,'', str(mano))
            #print(mano)
            # pass
            td.append(mano)
    return td
    # finding all <li> tags
   
# ------------------------------------------------------
#---------------------------------------------------
temples_data = []
templesearchkey = []
searchkey =[]

#-----------------------------------------------------
csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
   
    googledatastunindiadir = ''
    googledatastunindiadir = ("{}{}{}".format(googledataindiastutdir,N,statename))
    
    cre_directory = Path(googledatastunindiadir)
    cre_directory.mkdir(parents=True, exist_ok=True)
    templesserpapifilterdata = serapitemplesoutfile(st = statename,csvf ="Temples_Google_SerpApi.csv")
    GooglePaginationsSerplinks = serapitemplesoutfile(st = statename,csvf ="Google_Paginations_Links_SerpApi.csv")
#------------------------------------------------------------------------------------------------------------------
    linkcolumnname = ['Google SerApi Links']
    readdata = csvreaddata(GooglePaginationsSerplinks, str(linkcolumnname[0]))
    if (readdata):

        for l in (readdata):
            url = ''
            for x in l:
                    url += ''+ x
            
            templelinkdata = re.sub(r'^.+/([^/]+)$', r'\1', url)
            
            domainf = urlparse(url).netloc.split('.')[1]
            domainname = urlparse(url).netloc
            if (domainf):
                #print(netloc)
                if (domainf == 'google'):
                    #templename = googling(url,templelinkdata)
                    #if (templename):
                     #   temples_data.append(templename)
                    #print(urlparse(url).query)
                    patten = ("{}{}{}".format('&q=', "([^$]*)", '&sa='))
                    q = str(urlparse(url).query)
                    searchp = re.findall(patten, q)
                    if(searchp):
                        pass
                    else:
                        patten = ("{}{}{}".format('q=', "([^$]*)", '&ucbcb='))
                        q = str(urlparse(url).query)
                        searchp = re.findall(patten, q)
                    
                    mano = ''
                    for x in searchp:
                        mano += ''+ x
                    q = ''
                    q = re.sub(r'[^a-zA-Z]',' ',str(mano))
                    
                    searchkey.append(normalize_caseless(q))
                else:
                    
                    print(url)
                    mano = googling(url,domainname)
                    if(mano):
                        #print(mano)
                     
                        n = 0
                        for t in (mano):
                            #if (n != 0):
                            if (t not in templeslist):
                                templeslist.append(t)
                                q = ''
                                q = re.sub(r'[^a-zA-Z]',' ',str(t))
                                searchkey.append(normalize_caseless(q))
                            else:
                                print("Duplicate to be removed : ", t)
                                n =+ 1
                     
                            #print(mano[j])
                            #maj += ''+ j
                         
#--------------------------------------------------------------------
    readdata = ''
    templecolumnname = ['List of temples']
    readdata = csvreaddata(templesserpapifilterdata, str(templecolumnname[0]))
    if (readdata):

        for t in (readdata):
            #print(t)
            mano = ''
            for m in t:
                mano += ''+ m
                k = ''
                k = re.sub(r'[^a-zA-Z]',' ',str(mano))
                    
                searchkey.append(normalize_caseless(k))
#----------------------
fls = []                
for k in (searchkey):
    if (k not in templesearchkey):
        kls = []
        kls = k.split( )
        fls.append(kls)
        templesearchkey.append(k)
    else:
        pass
#-------------------------------
ct = []

for f in range (0,len(fls)):
    fs = (fls[f])
 
    for y in range(0,len(fs)):
       ct.append(fs[y])
# templesearchkey.append(k)

    #templedata = googling(search)
    #print(templedata)

#print(temples_data)
#l1 = ct


#print(ct)

filt = getfilters(ct)

print(filt)

#ddiff = DeepDiff(l1, l2, ignore_order=True)
#pprint (ddiff, indent = 2)
#print(fv)

