#!/usr/bin/env python3
import sys, json, requests, os
from flask import Flask, request, abort


app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.is_json:
        if request.method == 'POST':
            content = request.get_json()
            try:
                json_str = json.dumps(content)
                resp = json.loads(json_str)
                print (resp['commits'][0]['message'])
                for x in content:
                    if x == "commits":
                        print("Updating...")
                        print(json.dumps(content[x], indent=4, sort_keys=True))
                        # DO WHATEVER
                        os.chdir("/home/user/workspace/")
                        os.system("git pull origin master")
                        print("Up to Date! \n")
            except KeyError as erro:
                print(erro)
            return 'OK', 200
        else:
            abort(400)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=int("8081"), debug=True)
