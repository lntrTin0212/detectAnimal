from io import BytesIO
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16
from keras_preprocessing import image
from keras.layers import Input
import numpy as np
import pathlib
from PIL import Image
from skimage import io
from PIL import Image
import requests
# from . import cloudinary as cloudURL
import os

# from ..tutorialAPI import settings 
#to get the current working directory
# def runApp():
#     model = VGG16(weights='imagenet')
    
#     os.chdir("C:/Users/TKiTECH/Desktop/Lntr.tin/hoctap/LV/Django/tutorial/InveptionV3/animal")
#     directory = os.getcwd()
#     print("this is directory: ",directory)
#     data_dir = pathlib.Path(directory)

#     img_path = list(data_dir.glob('*'))
#     img = image.load_img(img_path[10], color_mode='rgb', target_size=(224, 224))
#     img.show()

#     x = image.img_to_array(img)
#     x.shape
#     x = np.expand_dims(x, axis=0)

#     x = preprocess_input(x)
#     features = model.predict(x)
#     p = decode_predictions(features)

#     return p[0]



def runAppPath(im):
    model = VGG16(weights='imagenet')
    response = requests.get(im)
    img = Image.open(BytesIO(response.content))
    img.show()
    img = img.save("testing1.png")
    directory = os.getcwd()
    data_dir = pathlib.Path(directory)
    data_dir = str(data_dir) + "\\testing1.png"
    print("DIRRRRRRRRR: ", data_dir)
    img = image.load_img(data_dir,color_mode='rgb', target_size=(224, 224))
    # img.show()

    x = image.img_to_array(img)
    x.shape
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    features = model.predict(x)
    p = decode_predictions(features)
    return p[0]

