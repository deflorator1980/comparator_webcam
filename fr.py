from pymongo import MongoClient
from bson.binary import Binary
import pickle
import face_recognition
import pickle
import sys
import os

client = MongoClient('localhost', 27017)
db = client.comparator
coll = db.faces   

filename = sys.argv[1]
known_image = face_recognition.load_image_file(filename)
known_encoding = face_recognition.face_encodings(known_image)[0]

## write faces
# descriptor = pickle.dumps(known_encoding)
# name_in_db = os.path.splitext(os.path.basename(filename))[0]
# coll.insert_one({"name": name_in_db, "face": descriptor})

## recognize faces
for person in coll.find():
    fe = pickle.loads(person["face"])
    result = face_recognition.compare_faces([fe], known_encoding)
    if result[0]:
        print("It's:", person["name"])
        sys.exit()
print('Person not found')

