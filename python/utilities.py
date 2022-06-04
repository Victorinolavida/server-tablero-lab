import requests
from bs4 import BeautifulSoup
import pandas as pd
import json 




def getByUrl(url):
    req = requests.get(url).content.decode('utf-8')
    return BeautifulSoup(req, 'html.parser')


def saveAsCsv(columnNames,data,pathFile,index=False):
    if(not pathFile): 
        return print('el nombre no puede ser valido')

    dictionary = {}
        
    if( len(columnNames) != len(data)):
        return print(' las columnas y la data en formato de lista deben ser de la misma logitud')
    
    for index in range(len(columnNames)):
        dictionary[columnNames[index]] = data[index]
    
    if(index):
        df = pd.DataFrame(dictionary)
        df.to_csv(pathFile)
        print('Archivo creado en ', pathFile)
    else:
        df = pd.DataFrame(dictionary, index=[i for i in range(len(columnNames))])
        df.to_csv(pathFile)
        print('Archivo creado en ', pathFile)





def saveAsHTML(soup):
    file = open('index.html','w')
    file.write(str(soup))
    file.close()
    print('se generó el archivo index.html')


def downloadImg(image_url,path, name,extension='png'):
    name = name.lower().replace(' ', '_')
    img_data = requests.get(image_url).content
    # print(f'{path}/{name}.{extension}')
    with open(f'{path}/{name}.{extension}', 'wb') as handler:
        handler.write(img_data)

def saveAsJson(columnNames,pathfile,data):
    jsonFile= {}
    for index in range(len(columnNames)):
        jsonFile[columnNames[index]] = data[index]

    f=open(pathfile+'.json','w')
    f.write(str(jsonFile))
    f.close()    
    # out_file = open(f'{pathfile}.json', "w") 
    
    # json.dump(jsonFile, out_file, indent = 6) 
    
    # out_file.close() 

    # print(pathfile)