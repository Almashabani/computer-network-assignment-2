# 📡 TCP Client-Server Application

## 👥 Group
Grupi 5

## 👥 Contributors
- Alma Shabani  
- Gjelbrim Morina 
- Altin Sollova

## 📌 Description
This project implements a simple TCP client-server communication system using Python.  
The server listens for incoming client connections, processes requests, and sends responses back to the client.

The system has been successfully tested in a real network environment using at least **4 different devices**, demonstrating reliable communication over TCP.

---

## ⚙️ Features
- TCP connection between client and server  
- Server listens on a specific IP and port  
- Client sends requests to the server  
- Server processes and responds to client messages  
- Tested with multiple devices in a real network  
- Basic command execution support  

---

## 🛠️ Technologies Used
- Python 3  
- Socket Programming (`socket` library)  
- TCP Protocol  

---

## 🚀 How to Run

### 1. Set the server IP address and port
Open `serverside.py` and set:

```python
hostname = "YOUR_SERVER_IP"
portno = YOUR_PORT
```
### 2. Configure the client
Open `clientside.py` and set the same IP address and port as the server:

```python
hostname = "YOUR_SERVER_IP"
portno = YOUR_PORT

```
## 💻 Commands

### For all users:
- LIST
- READ filename.txt
- EXIT

### For admin only:
- WRITE filename.txt some text
- EXEC file.py
