import socket
import sys
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3125))
print(s.recv(1024))

while True:
  message = str(raw_input())
  s.sendall(message)
  subprocess.call(["clear"])
  recieved = s.recv(1024)
  print(recieved)

  while(recieved[-1:] == '\n'):
    recieved = s.recv(1024)
    print(recieved)


s.close()