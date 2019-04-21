#!/usr/bin/env python3
import sys, json
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    print("webhook"); sys.stdout.flush()
    if request.method == 'POST':
        data = json.loads(request.json)
        try:
            for x in data:
                if x == "Branch":
                    print("%s: %s" % (x, data[x]))
        except KeyError as erro:
        print(erro)

        return 'OK', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
