# tcp_client.py
import socket

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
print("Socketi eshte gati i gjeneruar")

hostname = "172.16.100.239"
portno = 9997

mySocket.connect((hostname, portno))
print("Lidhja eshte arritur me serverin")