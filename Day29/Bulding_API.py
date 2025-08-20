#Exercices

from flask import Flask, Response, request
import json
import pymongo

from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)

# Remplace avec ton vrai lien MongoDB Atlas
MONGODB_URI = 'mongodb+srv://<username>:<password>@cluster.mongodb.net/test'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

# GET - tous les étudiants
@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    students = db.students.find()
    return Response(dumps(students), mimetype='application/json')

# GET - un étudiant par id
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student(id):
    student = db.students.find_one({"_id": ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

# POST - ajouter un étudiant
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    data = request.get_json()
    data["created_at"] = datetime.now()
    db.students.insert_one(data)
    return Response(dumps({"message": "Student created"}), mimetype='application/json')

# PUT - mettre à jour un étudiant
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    db.students.update_one({"_id": ObjectId(id)}, {"$set": data})
    return Response(dumps({"message": "Student updated"}), mimetype='application/json')

# DELETE - supprimer un étudiant
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(dumps({"message": "Student deleted"}), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
