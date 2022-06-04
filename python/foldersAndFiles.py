import os



directory = os.getcwd()
folder_data = directory+'/data'


exist_data = os.path.isdir( folder_data )


def createFolderByName(name):
  #existe la carpeta data
  if( not exist_data ):
    #si no existe la crea
    os.mkdir(folder_data)
    #y crei la carpeta name dentro de data
    os.mkdir(folder_data+f'/{name}')
  else:
    #si ya existe data , pero no existe la capeta "name"
    if( not os.path.isdir(folder_data+f'/{name}')):
      os.mkdir(folder_data+f'/{name}')
    
    return folder_data+f'/{name}'



def createFolderInData(name,parentFolder=''):
  if parentFolder:
    exist = os.path.isdir(  folder_data + '/' +  parentFolder )
    print( folder_data + '/' +  parentFolder )
    if( not exist ):
        os.mkdir(folder_data + '/' +  parentFolder)

    if not os.path.isdir( f'{folder_data}/{parentFolder}/{ name }' ):
        os.mkdir(f'{folder_data}/{parentFolder}/{ name }')

    return f'{folder_data}/{parentFolder}/{ name }'



