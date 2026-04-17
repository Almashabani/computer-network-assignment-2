
import socket
import os
import subprocess

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
print("Socketi eshte gjeneruar")

hostname = " "
portno = 0000

mySocket.bind((hostname, portno))
print("Socketi eshte i lidhur me IP Addressen specifike {} dhe me portin {}".format(hostname, portno))

mySocket.listen(5)
print("Jemi ne pritje te perdoruesve")