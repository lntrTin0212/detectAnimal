import cloudinary

from dotenv import load_dotenv
load_dotenv()

config = cloudinary.config(
    cloud_name = "dixv7ftex", 
    api_key = "276798584128424", 
    api_secret = "OStPjN4Fd-d0Sp-G6c_ieu8uu6g",
    secure = True
)

import cloudinary.uploader
import cloudinary.api

def cloud_URL(data):
  result = cloudinary.uploader.upload(data)
  return result