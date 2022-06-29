from email.mime import image
from msilib.schema import Error
import requests
import json
import os
import time


def current_milli_time():
    time_str = str(time.time() * 1000)
    return time_str[:8]

# Di Ubah disini untuk code sec atau masukan ke dalam variabel sec
with open("/Users/Mahesa/Documents/INI KULIAH BUKAN MAIN MAIN/Code/Pemograman/VS CODE/Python/API/code_sec.txt","r") as f:
    sec = f.read()

try:
    temp = {}
    dir = os.getcwd()
    file_name_success = os.path.join(dir,"Data Success")
    file_name_Failed = os.path.join(dir,"Data Failed")
    image_file_1 = input("File Directory Foto 1 : ")
    image_file_2 = input("File Directory Foto 2 : ")
    all_img = [image_file_1,image_file_2]
    for i in all_img:  
        with open(i, "rb") as f:
            im_bytes = f.read()
            temp[i] = im_bytes     
            f.close
            
    url = "https://api.advance.ai/openapi/face-recognition/v4/check"
    files = {'firstImage': temp[image_file_1],'secondImage':temp[image_file_2]}
    headers = { "X-ADVAI-KEY" : sec}
    r = requests.post(url = url, headers=headers,files=files)
    conver_to_json = json.dumps(r.json()['data'])
    if r.json()['data']['similarity'] > 60:
        print(f"Memiliki kemiripan dengan Confidence : {r.json()['data']['similarity']}")
        print(conver_to_json)
    else :
        print(f"Tidak Memiliki kemiripan dengan Confidence : {conver_to_json['data']}")
    
except Error as e:
    pass
    