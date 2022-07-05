import pandas as pd

import re
from pathlib import Path

#--------------------------------------------------------------------------
def prt(p):
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#--------------------------------------------------------------------------
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"

Project_Performed_Country = "indias"

projectname = "temples"

N = "\\"

#C:\google\serpapi\indias\data\Temples
#C:\google\serpapi\indias\data\Temples
#C:\google\serpapi\indias\data\Indias_googlengine_temple_States_and_UTs
#-------------------------------------------------------------------------------

Application_Data_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,"data"))

Google_States_UT_Data_Folder_Path = ("{}{}{}{}{}".format(Application_Data_Folder,N,Project_Performed_Country.capitalize(),'_',"googlengine_temple_States_and_UTs"))
#------------------------------------------------------------------------------------
googledataindiastutdir = ("{}{}{}".format(Application_Data_Folder,N,projectname.capitalize()))

templeinputfiletext = ("{}{}{}".format(googledataindiastutdir, N, "temples.txt"))
#------------------------------------------------------------------------------------
#print(templeinputfiletext)
cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)
#-----------------------------------------------------------------------------
indiastautfile = ("{}{}{}".format(Google_States_UT_Data_Folder_Path,N,"Ind_googlengine_states_ut_master.csv"))
#----------------------------------------------------------------------------------------------------
path = Path(indiastautfile)
#----------------------------------------------------------------------------------------------------
if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
else:
    pi="\'Data of States and UTs is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    exit(1)
#-----------------------------------------------------
fields = ['States and Union Territories in India']
#----------------------------------------------------------------------------------------------------
df_stuts = pd.read_csv(indiastautfile, skipinitialspace=True, usecols=fields)
#-----------------------------------------------------
statesget = sorted([list(row) for row in df_stuts.values])
sul =  []
cap = []
templeslisings = []
#----------------------------------------------------------------------------------------------------
for t in statesget:

  m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
  
  if m not in sul:
      sul.append(m[0])
      cap.append(m[1])
  else:
        print("Duplicate is removed", t)
#----------------------------------------------------------------------------------------------------
csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
    capital = re.sub(patternspace, '-', cap[cc])

templefilepushtxt = ("{}{}{}".format(statename,'_',"templewebfile.txt"))

templefilegiventxt = ("{}{}{}".format(googledataindiastutdir,N,templefilepushtxt))


#df = pd.read_csv(inputfile, delimiter=',', encoding='encoding')

df_temples = pd.read_csv(templeinputfiletext, skipinitialspace=True)

templeslist = ([list(row) for row in df_temples.values])

def removen(string):

    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r"[^a-zA-Z<>:';2315{}/\-1]+", ' ', k) for k in clean_string.split("\n")]
        mymano = ' '
        for x in clean_string:
            mymano += ' '+ x
        #print(mymano)
        return mymano

tmol = []

state = re.sub('-',' ', statename)
title = ("{}{}{}".format("<html><head> <title> Famous Temples in  ", state, " </title>"))
clean_string = removen(title)
tmol.append(clean_string)


qq = """
<style>
h3 { 
color: blue; 
font-family: 'Helvetica Neue', sans-serif; 
font-size: 15px; font-weight: bold; 
letter-spacing: -1px; 
line-height: 2; 
text-align: left; 
}

</style>

</head>
<body>
"""

clean_string = removen(qq)
tmol.append(clean_string)

temples  =  []

def capitalize_words(text):
    return text.capitalize()

def capitalize_sp(text):
    return " ".join([i.capitalize() for i in text.split(' ')])

ttc = []

for l in range(0,len(templeslist)):
  
    temple = re.sub(r"[^a-zA-Z]+",' ', str(templeslist[l][0]))
    temple = capitalize_sp(temple)
    location = re.sub(r"[^a-zA-Z]+",' ', str(templeslist[l][1]))
    location = capitalize_sp(location)
    mano = ("{}{}{}{}{}".format("<h3>", temple, ',', location, "</h3>"))
    ttc.append(mano)

for o in (ttc):
  
    tmol.append(o)


tmol = " ".join(str(elem) for elem in tmol).strip()


with open(templefilegiventxt, 'w') as tfile:
    tfile.write(tmol)

pi="\'The Temple Web File is Generated  \' :"
p = ("{} {}".format(pi,templefilegiventxt))
prt(p)