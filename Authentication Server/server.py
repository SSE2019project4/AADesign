import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#create a socket for the client to connect to
port = 3125
s.bind(('0.0.0.0', port))									#bind socket to port 3125
print ('Socket Binded to Port 3125')
s.listen(10)												#listen on server for a connection							
print ('Socket is Listening')	

c, addr = s.accept()										#accept all connections over the port
print('Connection Established')

users = []													#user table
users.append(('admin', 'secret', '0'))						#default admin
signed = ('', '', '1')

while True:
    while signed[0] == '':									# while you are not signed in
        
        c.sendall('\033[1;34;40m1) Register Account\n2) Sign In\n4) Exit\033[0;37;40m')
        options = c.recv(1024)								#recieve the option from the client

        if options == '1':									#register account
            c.sendall('Register Account\nName:')
            name = c.recv(1024)								#request and recieve name and password of new account
            c.sendall('Password:')
            password = c.recv(1024)

            users.append((name,password, '1'))				#add credentials to the user table
            print("New Account Added : "+name + ' (' + password + ')')
            c.sendall('Account Successfully Created!\n')
        
        elif options == '2':								#sign in
            c.sendall('Sign In\nName:')
            name = c.recv(1024)								#request and recieve sign in credentials

            c.sendall('Password:')
            password = c.recv(1024)

            flag = False
            for a in users:									#iterate over user table and see if credentials match
                if name == a[0] and password == a[1]:
                    signed = a 								#credentials match, sign the user in
                    flag = True 
            if flag == False:								#credentials do not match any user, send an error me
            	print('\033[1;31;40mAttempted login '+ name + '(' + password + ')\n\033[		0;37;40m')
                c.sendall('\033[1;31;40mAccount does not exist, check username and password\n\033[0;37;40m')
        
        elif options == '4':								#close the connection to the server
            c.sendall("\033[1;31;40mExiting\033[1;37;40m")
            c.close()

    c.sendall('\033[1;32;40mSigned in as ' + signed[0] + '\n\033[1;34;40m1) Sign Out\n2) Show Users\n4) exit\033[1;37;40m')		#the user is now signed in
    options = c.recv(1024)

    if options == '1':			#sign out
        signed = ''
    
    elif options == '2':		#request to see user table, but be signed in as administrator, else error message
		if signed[2] == '0': 
			for a in users:		#iterate and print all users in the table
				c.sendall(a[0]+'\n')
		else:
			c.sendall('\033[1;31;40mYou are not authorized to use that function\n\033[0;37;40m')		#send the error message to the client 
			print('\033[1;31;40mUnauthorized access of user table from : '+ signed[0] + '\033[0;37;40m')	#print an error message to the console

    elif options == '4': 	#close the connection to the server
        c.close()
