"""
Google Engine Search by SerpAPI 
Python : Parse JSON file of SerpAPI, which is created by the Google search.
_____________________________________________________________________________

Project contact: Google Cloud Search API, Kyndryl
Email: Ramamurthy.valavandan@kyndryl.com
Project : Python API for Google Search Engine

Use Case: 
-----------
Creating the vaccination list of Covid-19 and visualization of json.
Program : parseserpapijsonvaccination.py
----------------------------
This program is written in Python Language
Created for Lab purposes with regulations of Nature Labs

Purpose: 
----------
This program is an extension of generating the JSON file based on WHO - Vaccination
Google Search Engine API – SerpAPI. 
Google Search Key: Covid-19 Vaccination types 
JSON file input: vaccination.json
https://chart-builder.data.world/?dataset=gcp%2Fbig-query&query=SELECT%20DISTINCT%28vaccines_used%29%20as%20Vaccines%0D%0AFROM%20vaccination_data%0D%0AGROUP%20by%20vaccines_used%0D%0AORDER%20by%20vaccines_used&query_type=SQL&saved_query=6c035664-5e80-4bdb-a21d-8a68494735f7
This program is used to parse JSON file, which is generated by Google Search API (SerpAPI) 
JSON file has the information of the Google Search Engine.
Create the necessary folders in local and download and save JSON for locally parse the search key.
Generate two CSV files will be generated from Google Search Engine JSON.
1)	vaccincation.json
2)	C:\google\serpapi\indias\data\Medicine

Functionalities:
---------------
After connecting to Google Search Engine API the JSON is generated
https://chart-builder.data.world
This program is used to connect Google Search API (SerpAPI) 
Download the searched information which is saved in the JSON file based on the Google Search Engine.
Create the necessary folders in local and download and save JSON for locally parse the search key.
---------------------------------------------------------------------------------------------------
SerpAPI Sponsorship:
--------------------
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
Nature Labs : Google Engine @ SerApi, LLC.

Download from Git Hub

https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py

How to use
------------
python parseserpapijson.py

Contact 
--------
Kyndryl GCP Guild Moderator: Ramamurthy V 
Email: ramamurthy.valavandan@kyndryl.com
GCP Contact: gcpguild@gmail.com
Date: June 21, 2022.
Revised : July 8, 2022
Contributors: 22 key members from Google Cloud Search API.

For SerpAPI Key request, please write an email request with an email subject of 'request for SerpApi Key'

Email: ramamurthy.valavandan@kyndryl.com
"""
#-----------------------------------------------------#-----------------------------------------------------
githubserpaijson = "https://github.com/NATURE-LABS/temples/blob/main/serpapijsongetlocal.py"

serpapitemplestutindiagoogle = ['vaccination.json']

import json, re, csv, unicodedata,  string

from pathlib import Path


import pandas as pd



headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

#C:\google\serpapi\indias\data\Medicine
rootpath = "C:"
client="google"
sponsor = "serpapi"
N="\\"
Project_Country = "indias"
Project_ID = "Medicine"
max_gs = 10 # maximum number of google search in href or urls
#-----------------------------------------------------
medicine_data_dir = ("{}{}{}{}{}{}{}{}{}{}{}".format(rootpath,N,client,N,sponsor,N,Project_Country,N,"data",N,Project_ID))

cre_directory = Path(medicine_data_dir)
cre_directory.mkdir(parents=True, exist_ok=True)

medicinejson = ("{}{}{}".format(medicine_data_dir,N,"vaccination.json"))
medicinecsvout = ("{}{}{}".format(medicine_data_dir,N,"vaccination_list.csv"))
#-----------------------------------------------------

path = Path(medicinejson)

if not path.is_file():
    pi="\'Medicine data is missing: \' :"
    p = ("{} {}".format(pi,medicinejson))
    prt(p)
    exit(1)
#-----------------------------------------------------
vaccination_data = []
with open(medicinejson) as fh:
    data = json.load(fh)
       
    for d in (data):
        try: 
            vacdata = data ["data"]["values"]
            for v in (vacdata):
                if v["Vaccines"] not in (vaccination_data):
                    vaccination_data.append(v["Vaccines"]) if v["Vaccines"] else []
        except KeyError: pass  

def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,'', clean_string)
        #clean_string = [re.sub(r"[^a-zA-Z,-]+",'', clean_string)]
        mymano = ''
        for x in clean_string:
            mymano += ' '+ x
        #print(mymano)
        return mymano

vaccin_company = []
for v in  (vaccination_data):
    #print (v)
    v = v.split(',')

    for n in range(0,len(v)):
        cld = (v[n]).strip()
        if cld not in (vaccin_company):
                vaccin_company.append(cld)
             
vaccin_company_sorted = sorted(vaccin_company)

vpss = []
for v in (vaccin_company_sorted):
    if (v == 'Turkovac'):
        vc = v
        va = 'ERUCOV-VAC'
    else:
        vp = v.split('-')
        vc = vp[0]
        va = vp[1]

    pi = [vc, va]
    vpss.append(pi)

temple_rw = pd.DataFrame(vpss)
header =  ['Companies', 'Vaccinations']
mode = 'w' if header else 'a'
temple_rw.to_csv(medicinecsvout, encoding='utf-8', mode=mode, header=header)



pi="\'Covid-19 Vaccination data is generated  \' :"
p = ("{} {}".format(pi,medicinecsvout))
prt(p)