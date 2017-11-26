![alt text](https://images-na.ssl-images-amazon.com/images/I/51KuWa6FVQL._SY355_.jpg) ![alt text](http://qualityshoppingmall.com/wp-content/uploads/2017/01/Ankuoo-NEO-Smart-Plug-Wi-Fi-White-0-2.jpg)

# Overview
Exposes a basic HTTP interface to enable / disable the plug

## The hardware

After lots of research, I discovered these devices are basically clones of the cheap Chinese Broadlink wifi plug.
Thankfully @mjg59 created an awesome library that allows us to communicate with these devices.

It should work with the following devices
* Watts Clever Wifi Plug
* Ankuoo NEO Smart Plug Wi-Fi
* All other cheap Ankuoo plugs (please test?)
* Broadlink 

## Prerequisites
* [python-broadlink](https://github.com/mjg59/python-broadlink) - Amazing work! Used to communicate with the plug
* [flask](http://flask.pocoo.org/) - Used for the simple webserver

Install using pip
* pip install broadlink
* pip install flask

## Find your plug's mac and IP address
If you have the "InPlug" app installed, it will display the mac address of the device. Go to your router's admin and look at the DHCP table, you should be able to find the IP address of the device there. It's best practice to setup a static lease for this mac address so the plug always has the same IP address.
## Setup
Usage is as follows (remove any : from the mac address, for example 01:02:03:04:05 will be as follows)

run.py -ip 192.168.1.5 -mac 0102030405

Now access http://localhost:4020/

There is an optional parameter -port and this allows you to specify the port the webserver will listen on.
## Usage
The HTTP GET commands are as follows
* / - will give you the current status
* /turnon - turns on the plug
* /turnoff - turns off the plug

## My usage

I have [HA Bridge](https://github.com/bwssytems/ha-bridge) running in a docker container, this allows me to control this plug with Alexa.
