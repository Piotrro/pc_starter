from decoder import decrypt
from wake_on_lan_tools import wake_pc

from flask import Flask, request, render_template, Response
import os


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello() -> str:
    return 'Hello from the PAAA home app!'


@app.route("/run_pc", methods=['GET'])
def run_pc_get():
    return render_template('form.html')


@app.route("/run_pc", methods=['POST'])
def run_pc() -> str:
    data = request.get_json()
    encrypted_mac = data.get("MAC")
    key = os.environ.get('RUN_PC_PASSWD', "").encode()
    if not key:
        print("No secret key in environ!!")
        return Response(status=405)
    mac = decrypt(encrypted_mac, key).decode()
    if mac:
        print(mac)
        # wake_pc(mac)
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='192.168.0.136', port=5000, debug=False)
    # app.run(host='0.0.0.0', port=5000, debug=True)
