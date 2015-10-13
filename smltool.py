import re
import socket

IP_ADDRESS = '127.0.0.1'     # ip address of your device
PORT = 5000                  # port of your device
BUFFER_SIZE = 1024


def parse_sml(data):
    reg15_7_0 = re.compile('0701000F0700.{16}(.{8})0177')
    reg1_8_0 = re.compile('621E52FF56.{10}01')

    arr15_7_0 = re.search(reg15_7_0, data)
    arr1_8_0 = re.search(reg1_8_0, data)

    s = arr15_7_0.group(0)
    print(s)
    int15_7_0 = int(s[1], 16)
    s = arr1_8_0.group(0)
    print(s)
    int1_8_0 = int(s[1], 16) / 1000

    print(("Wirkleistung momentan: " + str(int15_7_0) + " Watt"))
    print(("Gesamt Bezug: " + str(int1_8_0) + " kW"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((IP_ADDRESS, PORT))
    print("Connected...")

    while True:
        data = sock.recv(BUFFER_SIZE)
        parse_sml(data)
except:
    print("Connection failed!")
    sock.close()
