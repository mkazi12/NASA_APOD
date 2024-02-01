# This program takes the api key from the NASA APOD Website and displays it in the terminal
#
# @author Maroof Kazi

import json as js
import requests 
from PIL import Image
from imgcat import imgcat
import numpy
import urllib.request
import certifi

# this url gets the NASA APOD image
url = 'https://api.nasa.gov/planetary/apod?api_key=IhkBY8JNoyICFkGoHBCvXNdgh8f8M4MmMVAhBcCm'

# requests information about the url
v = requests.get(url)
# gets the actual image from the url
data = v.json()['url']

# creates and prints the image as an array 
im = numpy.asarray(Image.open(urllib.request.urlopen(data)))
print(type(im),im.shape, im.dtype)

# uses imgcat to display the image in enriched terminal
imgcat(im)

