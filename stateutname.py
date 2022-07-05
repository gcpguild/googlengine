import pandas as pd
import re
from pathlib import Path
#--------------------------------------------------------------------------
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"
Project_Performed_Country = "indias"
projectname = "temples"
N = "\\"
#-------------------------------------------------------------------------------
Application_Data_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,"data"))
Google_States_UT_Data_Folder_Path = ("{}{}{}{}{}".format(Application_Data_Folder,N,Project_Performed_Country.capitalize(),'_',"googlengine_temple_States_and_UTs"))
#------------------------------------------------------------------------------------
googledataindiastutdir = ("{}{}{}".format(Application_Data_Folder,N,projectname.capitalize()))
#------------------------------------------------------------------------------------
cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)
#-----------------------------------------------------------------------------
indiastautfile = ("{}{}{}".format(Google_States_UT_Data_Folder_Path,N,"Ind_googlengine_states_ut_master.csv"))
#----------------------------------------------------------------------------------------------------
path = Path(indiastautfile)
#----------------------------------------------------------------------------------------------------
if path.is_file():
    pass
else:
    exit(1)
#---------------------------------------------------------------------------------
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
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r"[^a-zA-Z,]+",'', clean_string)]
        mymano = ''
        for x in clean_string:
            mymano += ' '+ x
        #print(mymano)
        return mymano
#-----------------------------------------------------------------
csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
  
    capital = re.sub(patternspace, '-', cap[cc])
    st = removen(statename)
    cp = removen(cap[cc])
    stc = ("{}{}{}".format(st,',',cp))
    stc = removen(stc)
    print(stc)