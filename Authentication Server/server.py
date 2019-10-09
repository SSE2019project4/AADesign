import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
s.bind(('0.0.0.0', port))
print ('Socket Binded to Port 3125')
s.listen(10)
print ('Socket is Listening')

s.settimeout(10)
c, addr = s.accept()
print('Connection Established')

users = []
signed = ''
while True:
    while signed == '':
        
        c.sendall('\033[1;34;40m1) Register Account\n2) Sign In\n3) Print Users\n4) Exit\033[0;37;40m')
        options = c.recv(1024)

        if options == '1':
            c.sendall('Register Account\nName:')
            name = c.recv(1024)
            
            c.sendall('Password:')
            password = c.recv(1024)

            users.append((name,password))
            print("New Account Added : "+name + ' (' + password + ')')
            c.sendall('Account Successfully Created!\n')
        
        elif options == '2':
            c.sendall('Sign In\nName:')
            name = c.recv(1024)

            c.sendall('Password:')
            password = c.recv(1024)

            flag = False
            for a in users:
                if name == a[0] and password == a[1]:
                    signed = a[0]
                    flag = True 
            if flag == False:
            	print('\033[1;31;40mAttempted login '+ name + '(' + password + ')\n\033[		0;37;40m')
                c.sendall('\033[1;31;40mAccount does not exist, check username and password\n\033[0;37;40m')

        elif options == '3':
            for a in users:
                c.sendall(a[0]+'\n')
        
        elif options == '4':
            c.sendall("\033[1;31;40mExiting\033[1;37;40m")
            c.close()

    c.sendall('\033[1;32;40mSigned in as ' + signed + '\n\033[1;34;40m1) Sign Out\n4) exit\033[1;37;40m')
    options = c.recv(1024)

    if options == '1':
        signed = ''
    elif options == '4': 
        c.close()