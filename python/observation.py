import json
from utilities import *

soup = getByUrl('https://observation.org/stats/')

""" las tables en esta base de datos son de la forma 

<table>

    <tr>
        <td> algo </tr>
        <td class="text-rigth"> numeros </td>
    </tr>

</table>

"""

tables = soup.find_all('table')
titles = soup.find_all('h2')
title_text = []

for title in titles:
  
    title_text.append(title.text)

def getData(table):
    trs = table.find_all('tr') #encontrado los <tr></tr>
    tds_tags = []
    tds_counts = []


    for tr in trs:
        tds = tr.find_all('td')
        for td in tds:
            data = td.text
            if( td.get('class') and 'text-right' in td.get('class') ):
                num = int( data.replace(',',''))
                tds_counts.append(num)
            else:
                exp = data.replace('\n','').replace(' ','').replace('\xa0','')
                tds_tags.append(exp)

    return [tds_tags,tds_counts]



dic = {}

for index in range(len(tables)):
    data = getData(tables[ index ])
    dic[title_text[index]]={
        'labels': data[0],
        'values': data[1]
    }


print( json.dumps( dic ) )
