from utilities import *

url = 'http://geneontology.org/stats.html#annotations:H0H0Oq8FEeyTdyuEnMB9Xw'

soup = getByUrl(url)


print(soup)


f = open('index.html','w')

f.write(str(soup))

f.close()