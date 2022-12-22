import socket

target_host = "www.google.pl"
target_port = 80

#Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to client
client.connect((target_host, target_port))

#Sending data
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode('utf-8'))

#Data acquisition
response = client.recv(4096).decode('utf-8')

print(response)