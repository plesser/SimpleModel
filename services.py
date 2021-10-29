from flask import Flask, request

from libs.run_model import process_score

ws = Flask(__name__)


@ws.route('/auto_base', methods=['POST'])
def hello_world():  # put application's code here
    res = process_score(request)
    return res

if __name__ == '__main__':
    ws.run(debug=True, host='0.0.0.0', port=5000)
    #ws.run(debug=True, host='localhost', port=5000)
