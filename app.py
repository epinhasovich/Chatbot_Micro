from flask import Flask, request, jsonify, render_template
import os
import random
import requests
import json


responses = ("Yooooooo", "Holla", "Sup?", "The sky is blue", "Let's get Schwifty", "Wubba Lubba Dub Dub")

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

# communicating with other bots w/ front-end
@app.route("/message/", methods=["GET"])
def message():
    if request.method == "GET":
        user_input = request.args.get('message')
        print(user_input)
        response = requests.get("https://immense-thicket-73815.herokuapp.com/message/?message=" + user_input)
        json_string = json.loads(response.content)
        print(json_string)
        print(response)
        response_message = {json_string["message"]}
        print(response_message)
        return response_message
    else:
        print("FAIL")
        return "FAIL"


# communicating with other bots
# app = Flask(__name__)
# @app.route("/message/")
# def message():
#     if request.args.get('message'):
#         user_input = request.args.get('message')
#         response = requests.get("https://immense-thicket-73815.herokuapp.com/message/?message=" + user_input)
#         json_string = json.loads(response.content)
#         print(json_string)
#         print(response)
#         response_message = {json_string["message"]}
#         print(response_message)
#         return str(response_message)
#     else:
#         return "Say Something in my URL for me to respond!"


# parrot
# app = Flask(__name__)
# @app.route("/message/")
# def message():
#     message = request.args.get('message')
#     return message


# drunk chat
# app = Flask(__name__)
# @app.route("/message/")
# def message():
# if request.args.get('message'):
#     return random.choice(responses)
# else:
#     return "Say Something in my URL"


# broken record
# app = Flask(__name__)
# @app.route("/message/")
# def message():
# if request.args.get('message'):
#     return "Broken Record..."
# else:
#     return "Say Something in my URL for me to respond!"


if __name__ == "__main__":
    local = "127.0.0.1"
    heroku = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))
    app.run(host=heroku, port=port)