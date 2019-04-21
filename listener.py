#!/usr/bin/env python3
import sys, json, requests
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.is_json:
        if request.method == 'POST':
            content = request.get_json()
            try:
                for x in content:
                    if x == "Branch":
                        print("%s: %s" % (x, content[x]))
                        r = requests.get(url = "http://localhost/chain", params = "{ 'address': 'http://localhost' }")
                        data = r.json()
                        print(json.dumps(data, indent=4, sort_keys=True))
            except KeyError as erro:
                print(erro)
            return 'OK', 200
        else:
            abort(400)


if __name__ == '__main__':
    app.run()
