from utilities import *
import re


soup = getByUrl('http://shiny.imbei.uni-mainz.de:3838/trend-db/')


scripts = soup.find_all('script')
divs = soup.find_all('div')



count = []



for i in range(len(scripts)):
    if( '{"x":{"count":' in scripts[i].text ):
        x = re.findall('"count":[0-9]*', scripts[i].text)
        num = x[0].replace('"count":', '')
        count.append(int(num))


print(json.dumps({
    'labels':['conditions','APA-events', 'genes affected by APA in cells of neuronal origin' ],
    'values':count
}))


