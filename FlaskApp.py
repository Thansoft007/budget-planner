from flask import Flask
from os import environ
import json

app=Flask(__name__)

@app.route("/")
def testing():
    x={'Name':'ThanSoft','Wife':'Divya','age':'27','message':'I love you'}
    return json.dumps(x)

if __name__ == "__main__":
    app.run(debug=False,port=environ.get('PORT',5000),host="0.0.0.0")