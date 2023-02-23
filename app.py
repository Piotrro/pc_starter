from decoder import decrypt
from wake_on_lan_tools import wake_pc

from flask import Flask, request, render_template, Response
import os


app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """
    Dummy endpoint to check if the app is online.

    :return:
    """
    return 'Hello from the PAAA home app!'


@app.route("/run_pc", methods=['GET'])
def run_pc_get():
    """
    Renders template with form to get data from user.

    :return:
    """
    return render_template('form.html')


@app.route("/run_pc", methods=['POST'])
def run_pc() -> Response:
    """
    Gets data from user, decrypts it and wakes up the PC.

    :return:
    """
    data = request.get_json()
    encrypted_mac = data.get("MAC")
    key = os.environ.get('RUN_PC_PASSWD', "").encode()  # "" instead of None because encoding to bytes.
    if not key:
        print("No secret key in environ!!")
        return Response(status=405)
    mac_or_name = decrypt(encrypted_mac, key).decode()
    mac = os.environ.get(mac_or_name.upper(), mac_or_name)  # If shortcut was given by user.
    if mac:
        wake_pc(mac)
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='192.168.0.136', port=5000, debug=False)  # prod
    # app.run(host='0.0.0.0', port=5000, debug=True)  # dev
