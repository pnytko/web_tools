import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0

def main():
    global listen
    global port
    global execute
    global target
    global upload_destination

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu")
    except getopt.GetoptError as err:
