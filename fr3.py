import face_recognition
import pickle
import postgresql
import sys
import os

filename = sys.argv[1]
known_image = face_recognition.load_image_file(filename)
known_encoding = face_recognition.face_encodings(known_image)[0]

db = postgresql.open('pq://postgres:postgres@localhost:5432/comparator3')

################dataset###########################3
# x = db.execute("CREATE TABLE faces (id SERIAL PRIMARY KEY, " "name VARCHAR(50), " "face BYTEA)")

# ins = db.prepare("INSERT INTO faces (name, face) VALUES ($1, $2)")
# name_in_db = os.path.splitext(os.path.basename(filename))[0]
# ins(name_in_db, pickle.dumps(known_encoding))

##############recognition########################
face_encodings = db.query("SELECT name, face FROM faces")

for i in range (0, len(face_encodings)):
    fe = pickle.loads(face_encodings[i][1])
    result = face_recognition.compare_faces([fe], known_encoding)
    if result[0]:
        print("It is ", face_encodings[i][0])
        sys.exit()

print("Person not found")