from bs4 import BeautifulSoup
import urllib.request
import re


links = []

titles = []
def getweburls(inputlink,sut):

    parser = 'lxml'  # or 'lxml' (preferred) or 'html5lib', if installed
    resp = urllib.request.urlopen(inputlink)
    soup = BeautifulSoup(resp, parser)
    if (sut == 'India'):
        titles.append(soup.title.string)
    #soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
    return soup

baselink = "https://www.googlengine.com"
soup = getweburls(inputlink = baselink, sut = 'Googlengine')

for link in soup.find_all('a', href=True):
    fulllink = ''
    lh = ''
    lh = link['href']
    lh = re.sub('/','',lh)

    conditions = [len(lh) == 3, lh[-1] == 't']

    if all(conditions):
        fulllink = ("{}{}{}".format(baselink,'/',lh))
   
        if not fulllink in links:
            links.append(fulllink)
          

fullcalls = []

for l in range(0, len(links)):
    soup = getweburls(inputlink = links[l], sut = 'India')
    print(links[l], titles[l])