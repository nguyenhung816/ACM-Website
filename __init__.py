from flask import Flask, jsonify, abort, make_response, request
import json

app = Flask(__name__)

@app.route('/processjson', methods=['POST'])
def process():
    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result':'success', 'name':name, 'location':location, 'ramdomlist':randomlist})


if __name__ == 'main':
    app.run(debug=True)