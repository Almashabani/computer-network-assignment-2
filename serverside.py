
import socket
import os
import subprocess
import threading

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
print("Socketi eshte gjeneruar")

hostname = " "
portno = 0000

mySocket.bind((hostname, portno))
print("Socketi eshte i lidhur me IP Addressen specifike {} dhe me portin {}".format(hostname, portno))

mySocket.listen(5)
print("Serveri eshte ne pritje te perdoruesve..")

# Folderi ku klientet kane casje
SERVER_FOLDER = "server_files"
if not os.path.exists(SERVER_FOLDER):
    os.makedirs(SERVER_FOLDER)

# Klienti admin 
ADMIN_KEY = ["NETWORKADMIN2026"]

def process_command(client_name, role, command):
    parts = command.strip().split(" ", 2)
    if not parts or parts[0] == "":
        return "Komande e zbrazet."

    main_command = parts[0].upper()

    # LIST (lejohet per krejt klientet)
    if main_command == "LIST":
        files = os.listdir(SERVER_FOLDER)
        if not files:
            return "Folderi eshte bosh."
        return "File ne server:\n" + "\n".join(files)
    
# READ (lejohet per krejt klientet)
    elif main_command == "READ":
        if len(parts) < 2:
            return "Perdorimi: READ emri_file.txt"

        filename = parts[1]
        filepath = os.path.join(SERVER_FOLDER, filename)

        if not os.path.exists(filepath):
            return "File nuk ekziston."

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            return "Permbajtja e file-it '{}':\n{}".format(filename, content)
        except Exception as e:
            return "Gabim gjate leximit: {}".format(str(e))
        
    # WRITE (vetem admin)
    elif main_command == "WRITE":
        if role != "admin":
            return "Nuk keni privilegj WRITE. Ju keni vetem READ permission."

        if len(parts) < 3:
            return "Perdorimi: WRITE emri_file.txt teksti"

        filename = parts[1]
        text_to_write = parts[2]
        filepath = os.path.join(SERVER_FOLDER, filename)

        try:
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(text_to_write + "\n")
            return "Shkrimi ne file '{}' u krye me sukses.".format(filename)
        except Exception as e:
            return "Gabim gjate shkrimit: {}".format(str(e))
        
