# Import Module
import os

from cairosvg import svg2png

path = os.getcwd()

img = path + '/img'
svg = path + '/svg'


for file in os.listdir(svg):
  # print( svg + '/' + file)
  name = file.replace('svg','png')
  # f = open( svg + '/' + file, 'r'  )
  svg2png(url = svg + '/' + file, write_to = img + '/' + name )


# svg_code = """
#     <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
#         <circle cx="12" cy="12" r="10"/>
#         <line x1="12" y1="8" x2="12" y2="12"/>
#         <line x1="12" y1="16" x2="12" y2="16"/>
#     </svg>
# """



# svg2png(bytestring=,write_to='output.png')

# f = open(svg, "r")
# # print(f.readline())
# svg2png(url=svg,write_to=img)
# f.close()