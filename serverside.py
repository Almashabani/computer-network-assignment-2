
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

# Folderi ku klientet kane casje
SERVER_FOLDER = "server_files"
if not os.path.exists(SERVER_FOLDER):
    os.makedirs(SERVER_FOLDER)

# Klienti admin 
ADMIN_CLIENTS = ["John"]

def process_command(client_name, role, command):
    parts = command.strip().split(" ", 2)
    if not parts:
        return "Komande e zbrazet."

    main_command = parts[0].upper()

    # LIST (lejohet per krejt klientet)
    if main_command == "LIST":
        files = os.listdir(SERVER_FOLDER)
        if not files:
            return "Folderi eshte bosh."
        return "File ne server:\n" + "\n".join(files)