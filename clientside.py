# tcp_client.py
import socket

mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
print("Socketi eshte gati i gjeneruar")

hostname = "172.16.100.239"
portno = 9997

mySocket.connect((hostname, portno))
print("Lidhja eshte arritur me serverin")

# Jep emrin e klientit (John do jete admin)
client_name = input("Shkruaje emrin e klientit: ")
mySocket.send(client_name.encode())

msg_in = mySocket.recv(2048).decode()
print("\nPergjigja nga serveri:")
print(msg_in)

while True:
    print("\nShembuj komandash:")
    print("LIST")
    print("READ test.txt")
    print("WRITE test.txt Pershendetje nga klienti")
    print("EXEC program.py")
    print("EXIT")

    msg = input("\nShkruaj komanden qe deshiron ta dergosh ne server: ")
    print("Mesazhi i derguar ne server:", msg)

    mySocket.send(msg.encode())

    response = mySocket.recv(4096).decode()
    print("\nPergjigja nga serveri:")
    print(response)

    if msg.strip().upper() == "EXIT":
        break

mySocket.close()
print("Lidhja eshte arritur me sukses dhe komunikimi eshte bere me serverin")