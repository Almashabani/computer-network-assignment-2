# tcp_client.py
import socket

hostname = " "
portno = 0000

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socketi eshte gati i gjeneruar")

    mySocket.connect((hostname, portno))
    print("Lidhja eshte arritur me serverin")
except:
    print("Nuk mund te lidhet me serverin")
    exit()

# Jep emrin dhe admin key nese je admin
client_name = input("Shkruaje emrin e klientit: ")
admin_key = input("Shkruaj admin key nese je admin, perndryshe shtyp Enter: ")

login_data = client_name + "|" + admin_key
mySocket.send(login_data.encode())

msg_in = mySocket.recv(2048).decode()
print("\nPergjigja nga serveri:")
print(msg_in)

# Percaktimi i rolit nga mesazhi i serverit
if "admin" in msg_in.lower():
    role = "admin"
else:
    role = "read-only"

while True:
    print("\nKomandat e lejuara:")

    if role == "admin":
        print("LIST | READ | WRITE | EXEC | EXIT")
    else:
        print("LIST | READ | EXIT")

    msg = input(">> ")

    # Kontroll ne client-side per user normal
    if role != "admin":
        if msg.upper().startswith("WRITE") or msg.upper().startswith("EXEC"):
            print("Nuk ke privilegje!")
            continue

    mySocket.send(msg.encode())

    response = mySocket.recv(4096).decode()
    print("\nPergjigja nga serveri:")
    print(response)

    if msg.strip().upper() == "EXIT":
        break

mySocket.close()
print("Lidhja eshte mbyllur me sukses")