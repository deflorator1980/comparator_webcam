
from PIL import Image
import sys

mywidth = 500

img = Image.open(sys.argv[1])
wpercent = (mywidth / (img.size[0]))
hsize = int(img.size[1] * wpercent)
img = img.resize((mywidth, hsize), Image.ANTIALIAS)
img.save('resized.jpg')
