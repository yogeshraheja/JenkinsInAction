import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello and Welcome to Thinknyx DevOps Associate Program!"

@app.route('/feedback')
def hello():
    return 'We aim for 5 star rating from our learners!'

if __name__ == "__main__":
#    app.run()
    app.run(host="0.0.0.0", port=8080)
