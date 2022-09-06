import firebase_admin
from firebase_admin import credentials, db
import base64
import json
from datetime import datetime

class ConnectDb:
    def __init__(self, key = "key.json", dburl = None, HttpTimeOut = 30):
        self.__key = key
        self.__dburl = dburl
        self.HttpTimeOut = HttpTimeOut
        # logging in using private key
        if self.__dburl == None:
            raise ValueError("database url is required")
        
        cred = credentials.Certificate(self.__key) # json file certification
        firebase_admin.initialize_app(cred, {"databaseURL" : self.__dburl, "htttpTimeout" : HttpTimeOut})
        
    def upload_report(self, ref, file, status):
        with open(file, 'rb') as f:
            img = f.read()
        data = {"file" : base64.encodebytes(img).decode('utf-8'), "file_format": ref[-3:], "status" : status, "upload_time":datetime.now().strftime("%d-%m-%y %H:%M:%S")}
        root = db.reference(ref[:-4])
        root.set(data)

    def download_file(self, ref, path):
        root = db.reference(ref)
        data = root.get(ref)[0]
        file = data['file']
        with open(f"{path}{ref}.{data['file_format']}", 'wb') as f:
            f.write(base64.b64decode(file))
        return data
    def get_report(self, ref):
        root = db.reference(ref)
        data = root.get(ref)[0]
        data['file'] = base64.b64decode(data['file'])
        return data


