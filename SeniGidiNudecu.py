from nude import Nudity
from PIL import Image,ImageFilter

# Haram bro :D -O'K'

image = "girls.png"

im = Image.open(image)

nudity = Nudity()
isNude = nudity.has(image)

if isNude:
    im = im.filter(ImageFilter.GaussianBlur(radius=50))
    
im.show()