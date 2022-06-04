import re
from utilities import *


url = 'https://www.marinespecies.org/aphia.php?p=stats'
soup =  getByUrl(url)


#FOLDER IMAGES
# png_folder = createFolderInData('png',file_name)


# imgs = soup.find_all('img')
# try:
#     for img in imgs:
#        link = img.get('src')
#        alt  = img.get('alt')
#        if link and  'aphia.php' in link:
#         url = f'https://www.marinespecies.org/{str(link)}'
#         downloadImg( url, png_folder, alt  )
# except:
#     print('algo salio mal')

# aphia.php?



scripts = soup.find_all('script')

def getNumber(num):
    return int(num.replace('"',''))

def cleanItems(data):
    allnames = data[0].replace('allnames":','')
    allspecies =data[ 1 ].replace('"allspecies":','')
    acc_species = data[2].replace('"acc.species":','')
    acss_marine = data[3].replace('"acc.speciesnon-marine":', '')
    checkednames = data[4].replace('"Checkednames":', '').replace('"','')
    checkednames =checkednames.replace('%)','').split("(")
    checkednames[0] = getNumber(checkednames[0])
    checkednames[1] = getNumber(checkednames[1])
    return [getNumber(allnames), getNumber( allspecies ), getNumber( acc_species ), getNumber( acss_marine ), checkednames]


def getInfo(text):
    #names = re.findall('>([A-Z])\w+<',text)
    names = re.findall('>\w+<',text)[0]
    data = re.findall('allnames":".*"',text)[0]
    data =  data.split(',') 
    name = names.replace('<','').replace('>','')
    return [name, data]



text_clean=''
for script in scripts:
    if 'function getInitialData()' in script.text:
        text_clean = script.text.replace(' ','').replace('\n','')
        exp = re.search('functiongetInitialData()',text_clean)
        final = re.search('handleRowVisibility()',text_clean)
        text_clean = text_clean[exp.span()[0]:final.span()[1]]

## Limpiando otra el texto
text_clean = text_clean.replace('functiongetInitialData(){return[','').replace('];}functionhandleRowVisibility','')

text_split = text_clean.split('{"id"')


names = []
allnames = []
allspecies = []
acc_species = []
acss_marine = []
checkednames_value = []
checkednames_por = []


for par in text_split:

    if '<div' in par:
        try:
            #print(getInfo(par))
            data_list = getInfo(par)
            name = data_list[0]
            data_names = data_list[1]

            ## DATA A TRABAJAR
            names.append( name )
            allnames.append(cleanItems( data_names )[0])
            allspecies.append( cleanItems( data_names )[1] )
            acc_species.append( cleanItems( data_names )[2] )
            acss_marine.append( cleanItems( data_names )[3] )
            checkednames_value.append( cleanItems( data_names )[4][0] )
            checkednames_por.append( cleanItems(data_names )[4][1])
        except:
            print('')


data_clean = [names, allnames, allspecies, acc_species, acss_marine, checkednames_value, checkednames_por ]

columName = ['name',  'all names', 'all species', 'acc. species', 'acc. species non-marine','checked names(value)', 'checked names(percentage)']

dic = {
    columName[0]:data_clean[0],
    columName[1]:data_clean[1],
    columName[2]:data_clean[2],
    columName[3]:data_clean[3],
    columName[4]:data_clean[4],
    columName[5]:data_clean[5],
    columName[6]:data_clean[6],
}

print(json.dumps(dic))

