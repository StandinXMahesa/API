import requests
import json
import os
import time
import 

def current_milli_time():
    time_str = str(time.time() * 1000)
    return time_str[:8]

# Di Ubah disini untuk code sec atau masukan ke dalam variabel sec
with open("/Users/Mahesa/Documents/INI KULIAH BUKAN MAIN MAIN/Code/Pemograman/VS CODE/Python/API/code_sec.txt","r") as f:
    sec = f.read()

try :
    
    dir = os.getcwd()
    file_name_success = os.path.join(dir,"Data Success")
    file_name_Failed = os.path.join(dir,"Data Failed")
    image_file = input("File Directory : ")
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
        f.close

    url  ="https://api.advance.ai/openapi/face-recognition/v3/ocr-ktp-check"
    files = {'ocrImage': im_bytes}
    headers = { "X-ADVAI-KEY" : sec}
    r = requests.post(url = url, headers=headers,files=files)
    conver_to_json = json.dumps(r.json()['data'])
    
    if not os.path.exists(file_name_success):
        os.mkdir("Data Success")
    if not os.path.exists(file_name_Failed):
        os.mkdir("Data Failed")
        
    if r.json()['code'] == "SUCCESS":
        id = r.json()['data']['idNumber']
        name = r.json()['data']['name']
        time = current_milli_time()
        with open(file_name_success+'/'+ f"{time}" +f"_{id} - {name}.json", 'w+') as file:
            file.write(conver_to_json)
            file.close
    else :
        with open(file_name_Failed+'/'+"1.txt", 'w+') as file:
            file.write(conver_to_json)
            file.close
    print(f"Berhasil Terdetect \n{r.json()}")
except :
    pass