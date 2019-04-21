#!/usr/bin/env python3
import sys, json
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        if request.is_json:
            content = request.get_json()
            try:
                for x in content:
                    if x == "Branch":
                        print("%s: %s" % (x, content[x]))
            except KeyError as erro:
                print(erro)

            return 'OK', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
