import face_recognition
import pickle
import sqlite3
import sys
import os

filename = sys.argv[1]
known_image = face_recognition.load_image_file(filename)
known_encoding = face_recognition.face_encodings(known_image)[0]

con = sqlite3.connect('comparator.db')
cur = con.cursor()

## write faces
# cur.execute('create table if not exists faces (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), face blob)')
# name_in_db = os.path.splitext(os.path.basename(filename))[0]
# sql = 'insert into faces (name, face) values (?, ?)'
# cur.execute(sql, (name_in_db, pickle.dumps(known_encoding)))
# con.commit()

## recognize faces
cur.execute('select name, face from faces')
face_encodings = cur.fetchall()
for i in range (0, len(face_encodings)):
    fe = pickle.loads(face_encodings[i][1])
    result = face_recognition.compare_faces([fe], known_encoding)
    if result[0]:
        print("It's ", face_encodings[i][0])
        sys.exit()
print('Person not found')        
