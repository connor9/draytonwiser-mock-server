import flask
import os
import json

from mockwiser import WiserBaseAPI

def load_from_file(json_file):
    filename = os.path.dirname(__file__)
    with open(os.path.join(filename, '%s' % json_file), 'r') as f:
        return f.read()

data_file = load_from_file('config.txt')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
 
@app.route('/data/domain/', methods=['GET'])
def domain():
    data = load_from_file(data_file)
    return data

@app.route('/data/domain/<path:path>')
def catch_all(path):

    data = load_from_file(data_file)
    data = json.loads(data)
    
    wiser = WiserBaseAPI()
    data = wiser._parse_item_data(path, data)

    return flask.jsonify(data)

app.run(host= '0.0.0.0', port=5005)