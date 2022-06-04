from utilities import *
import re
import json


data = getByUrl('http://opig.stats.ox.ac.uk/webapps/stcrdab/')


script = data.find_all('script')[1]

datos = re.findall("data:.*", script.text)
patron = re.findall('labels:.*',script.text)


data=[]
labels=[]

for i in datos:
    row = i.replace('data: ',' ').replace('],','')
    row = row.replace('[','').split(',')
    if len(row) > 3:
        for j in range(len(row)):
            row[j]= int(row[j])
        data.append(row)

patron = patron[0].replace('labels: [','').replace('],','')
for i in patron.split(','):
    labels.append(int(i))


print( json.dumps( {
    'labels':['Cumulative total','Deposition per year','years'],
    'values':[data[0],data[1],labels]
} ) )