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
                    if x == "commits":
                        #data = print("%s: %s" % (x, content[x]))
                        print(json.dumps(content[x], indent=4, sort_keys=True))
                        # DO WHATEVER
            except KeyError as erro:
                print(erro)
            return 'OK', 200
        else:
            abort(400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8081"), debug=True)
