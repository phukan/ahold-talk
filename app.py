#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <head></head>
    <body><h1>app of ujjal phukan</h1></body>
    '''

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers['apikey'] == 'a3be1e29-8d95-474c-9ae8-faa88ade48b4':
        response = requests.get('http://noecommercews1098.cloudapp.net/api.ai/ordering.ashx', data = request.data)
        return response.text
    else:
        return 'foo'


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=True, port=port, host='0.0.0.0')
