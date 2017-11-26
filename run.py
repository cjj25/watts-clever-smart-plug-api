import broadlink # Used for communicating with the device
import time 
import codecs # Used for converting the mac address
from flask import Flask # Used for the web server
from sys import argv, exit # To get the command line parameters

# Quick and easy way of getting command line attributes
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts
commandArgs = getopts(argv)

mac = '';
ip = '';
port = '4020'

if '-ip' in commandArgs:
	ip = commandArgs['-ip']
else :
	print("Please provide the -ip parameter (IP address of the device on network)")
	exit();

if '-mac' in commandArgs:
	mac = commandArgs['-mac']
else :
	print("Please provide the -mac parameter (mac address of the plug, remove all ':')")
	exit();

if '-port' in commandArgs:
	port = commandArgs['-port']

mac=codecs.decode(mac,'hex')
devices = broadlink.sp2((ip, 80),mac)
devices.auth()


app = Flask(__name__)


@app.route('/')
def index():
	global devices
	return "Current status: " + str(devices.check_power())

@app.route('/turnon')
def turnon():
	global devices
	devices.set_power(True)
	return "Turned On"

@app.route('/turnoff')
def turnoff():
	global devices
	devices.set_power(False)
	return 'Turned Off'

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=port)