# PC Starter

Small Flask app which sends Magic Packets inside local network to run PCs.

You can configure your router to allow connection from out the lan to the app, so you can run your PC from anywhere.

### Prerequisites 

The app needs one env variable to work properly: `RUN_PC_PASSWD`. This is a variable containing master password to decode data sent by user.

You can also optionally set env variables (any name) containing the MAC address of your PC - it is used as alias for the MAC, so you don't have to remember it.

All requirements can be installed from `requirements.txt` file (`pip install -r requirements.txt`). The app was tested and developed on Python 3.7 and Python 3.10.

You would probably have to change IP address in the app.py as well as port of your choice. 

NOTE: You have to configure your PC to allow wake on lan to let the app run your PC(the process how to do it is different for each OS and BIOS).