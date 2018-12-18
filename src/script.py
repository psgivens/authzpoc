#!/usr/local/bin/python

print ("Hello World!!")

from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def test():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')    