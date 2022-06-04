from utilities import *
import re 
import requests
import pandas as pd
from foldersAndFiles import *

url = 'https://www.idigbio.org/home#annotations:LYYoBK8FEeyqii-vJybq2g'


soup = getByUrl( url )

script = soup.find_all('script')

primary = script[len(script)-3]

# saveAsHTML(soup)

url_raw = re.findall('url:.*',primary.text)[0]
url_clean = url_raw.replace('url: ' ,'')[:-1].replace('"','')


data = requests.get(url_clean).content.decode('utf-8')

names = re.findall('>.*<', data)
records = re.findall('a>.*Records', data)

for i in range(len(names)):
    names[i] = names[i][1:-1]

for i in range(len(records)):
    records[i] = records[i].replace(' Records','').replace('a>","','')
    records[i] = int(records[i].replace(',',''))


print(json.dumps({
    'labels':names,
    'values':records
}))