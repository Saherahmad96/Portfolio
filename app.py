from flask import Flask, jsonify

appname = Flask(__name__) 

@appname.route('/')
def homepage():
    return jsonify("hey im saher")

if __name__ == "__main__":
    appname.run(debug=True)




    

