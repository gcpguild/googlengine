"""
This program is written in Python Lanaguage
Created for Lab purpose with regulations of Nature Labs

-----------------
Usage : 
-------
Remove any Garbage and unncessary words for Google Search Engine
Create a CSV Data based on the grabage.txt in folder.

C:\google\serpapi\indias\data\Indias_googlengine_temple_States_and_UTs
grabage.txt should be placed in the above folder.

Example of grabage.txt
----------------------
have	has, have	had	had
 do	do, does	did	done
 is was and & * ( %) & 

Execution :
-----------
cd C:\google\serpapi\indias
python filters.py

Code History :
--------------
Code owner :
------------
Kyndryl Solution Private Limited
G1, 6th Floor, Manyata Tech Park
Bangalore, India
Developed by Google Cloud Architect : V Ramamurthy
Email : ramamurthy.valavandan@kyndryl.com
Google Cloud Research : gcpguild@gmail.com
Date : June 20, 2022
Latest version : 2.0
Date of final version : June 26, 2022.
"""
from gc import garbage
import re,unicodedata

import pandas as pd

from pathlib import Path

from itertools import compress

basepath = "C:"
codepath="google"
function = "serpapi"
N="\\"
namefile = "indias"
max_gs = 10 # maximum number of google search in href or urls

garbage_link = 'https://github.com/gcpguild/googlengine/blob/main/garbages.py'
worddatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))
datadirgoo = ("{}_{}".format(namefile.capitalize(),"googlengine_temple_States_and_UTs"))

worddatamasterdir = ("{}{}{}".format(worddatadir,N,datadirgoo))

cre_directory = Path(worddatamasterdir)
cre_directory.mkdir(parents=True, exist_ok=True)

garbage = ("{}{}{}".format(worddatamasterdir,N,"garbage_master.csv"))
wordmfile = ("{}{}{}".format(worddatamasterdir,N,"word_master.csv"))

def prt(p):
    
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

path = Path(garbage)

if path.is_file():
    pi="\'Garbage text file : \' :"
    p = ("{} {}".format(pi,garbage))
    prt(p)
    
else:
    pi="\'Garbage csv file is missing!\' :"
    p = ("{} {}".format(pi,garbage))
    prt(p)
    pi="\'Download :\' :"
    p = ("{} {}".format(pi,garbage_link))
    prt(p)
    
    exit(1)
#delimiter=' ',
columannames = ['Garbage List']
#sep="\s+|;|:|,|\\n",
df_garbage = pd.read_csv(garbage,
delimiter=',',
on_bad_lines='skip', 
engine="python",
skipinitialspace=True,
usecols=[columannames[0]]
)

garbages = sorted([list(row) for row in df_garbage.values])

listingwords =  []

for g in (garbages):
    
    g = re.sub(r'[^a-zA-Z]',' ',str(g))
    n = normalize_caseless(g)
    if n not in listingwords:
       listingwords.append(n)

listingwords = sorted(listingwords)

rw = pd.DataFrame(listingwords)
header =  ['List of words']
mode = 'w' if header else 'a'
rw.to_csv(wordmfile, encoding='utf-8', mode=mode, header=header)

wordcsvfile = Path(wordmfile)

if wordcsvfile.is_file():
    pi="\'Google filtered words data : \' :"
    p = ("{} {}".format(pi,wordcsvfile))
    prt(p)