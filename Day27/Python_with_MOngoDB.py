from flask import Flask, render_template
import os
import pymongo
MONGOSDB_URI = "mongodb+srv://*************:******************@30daysofpython.tkqvsv4.mongodb.net/?retryWrites=true&w=majority&appName=30DaysofPython"
print(MONGOSDB_URI)
client = pymongo.MongoClient(MONGOSDB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)