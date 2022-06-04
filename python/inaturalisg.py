import requests
import os
from utilities import *
from foldersAndFiles import *
from cairosvg import svg2png


file_name  = os.path.basename(__file__).replace( '.py' ,'')
path = createFolderByName(file_name)
print(path)


url = 'https://www.gbif.org/analytics/global'

soup = getByUrl(url)

imgs = soup.find_all('img')


for img in imgs:

    url = img.get('src')
    img_title = img.get('src').split('/')[-1].replace('.svg','')
    try:
        # downloadImg(url,path, img_title,'svg')
        svg2png(url = url, write_to = f'{path}/{img_title}.png' )

    except:
        print('Algo salio mal')
