*** how to use ***

1. run the server with 'python server.py'.

2. run the client with a second terminal using 'python client.py'.

3. follow the prompts on the client terminal.

*** notes ***

The Authentication aspect of the server is requiring a password for each account that wishes to access the site. this is done by registering an account from the client terminal.

The Authorization aspect of the server is the privilege level of the accounts that is by default 1, there is an existing account that is automatically added to the user table named 'admin' to use all privilegd functionality of the server, you must log in as the admin with the password secret. the admin has a privilege level of 0. the admin is the only account that can access and see the entries in the user table.

*** security measures ***
All misuse cases will result in a error message sent to the client and a warning message displayed in red in the server terminal. 

The identified misuse cases are: 
  signing into a non existing account. 
  exiting in the middle of a process.
  running a privileged command without the require privilege level.
  
