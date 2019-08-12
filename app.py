from pc_management.wake_on_lan_tools import wake_pc

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return 'Hello from the PAAA home app!'


@app.route("/run_pc", methods=['POST'])
def run_pc() -> str:
    data = request.get_json()
    wake_pc(data.get('MAC'))
    return 'Magic Packet was sent.'


if __name__ == '__main__':
    app.run(host='192.168.0.136', port=5000, debug=False)
