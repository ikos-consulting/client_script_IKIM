import requests
import os
from os import listdir
from os.path import isfile, join
import time
import json


def get_data(filename):
        f = open(filename,'rb') 
        string = f.read()   ### .replace('\n', '')
        f.close()
        return string
### define URL
url = 'http://localhost:5000/IKIM/api/v1.0/files'


### define 1 data path
data_path = "C:/Users/consultant/Desktop/IKIM/data_set_01/FichiersCBM/dcu1_VE1NV11"

os.chdir(data_path)

### get a list of all the file in the folder
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

### post each file

for client_file in onlyfiles:
    
        data_json = {'filename': client_file, 'data': str(get_data(client_file))}
        r = requests.post(url, json = data_json)
        
        print(r)
        time.sleep(1)


