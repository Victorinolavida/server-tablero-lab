from utilities import *
import requests,json,re
from foldersAndFiles import *

# file_name  = os.path.basename(__file__).replace( '.py' ,'')
# path = createFolderByName(file_name)



url = 'https://www.gbif.org/#annotations:OizqcK8FEeytlQuuU2IRWA'

# Occurrence records
url1 =  "https://api.gbif.org/v1/occurrence/search?occurrence_status=present" 


# Datasets
url2 = "https://api.gbif.org/v1/dataset/search"


#Publishing institutions
url3 = "https://www.gbif.org/api/publisher/count"

#Peer-reviewed papers using data
#https://www.gbif.org/resource/search?contentType=literature&literatureType=journal&relevance=GBIF_USED&peerReview=true



# data = json.loads( requests.get( url1 ).content.decode('utf-8') )


# print( data['count'] )


# url5 = "https://www.gbif.org/resource/search?contentType=literature&literatureType=journal&relevance=GBIF_USED&peerReview=true"


urls = [url1,url2,url3]
datos = [ ]
nombres = ["Occurrence records","Datasets","Publishing institutions"]

for  i in urls:
  
  data = json.loads( requests.get( i ).content.decode('utf-8') )


  datos.append(data['count'])


# el resultado no es lo que se busca #todo: mejorar
#saveAsCsv(nombres,datos,path+f'/{file_name}.csv', index=True)

print(json.dumps({
  'labels':nombres,
  'records':data
}))