
from utilities import *

soup = getByUrl("https://www.wikiaves.com.br/index.php") 

h3s = soup.find_all('h3')[2:5]
para = soup.find_all('p')[:3]




for index in range(len(h3s)):
    h3s[index] = int( h3s[index].text )
    para[index] = para[index].text


print(json.dumps({
    'labels':para,
    'values':h3s
}))

