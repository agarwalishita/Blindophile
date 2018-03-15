import json
import numpy as np
from clarifai.rest import ClarifaiApp
from gtts import gTTS
import os
import subprocess

language = 'en'
      
app = ClarifaiApp(api_key='d3986f9876b14a64a33605c4ab512d3e')
      
      # get the general model
model = app.models.get("general-v1.3")
      
      # predict with the model
response = model.predict_by_filename('bipin.jpg')

concepts = response['outputs'][0]['data']['concepts']
# parsed=json.loads(response)
# print parsed["name"]

DATA = ""

for concept in concepts:

    DATA += concept['name'] + "   "
print DATA
    # myobj.append([myobj])
myobj = gTTS(text=DATA, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
# os.popen("open welcome.mp3")

# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")