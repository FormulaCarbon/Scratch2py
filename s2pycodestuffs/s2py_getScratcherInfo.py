from scratch2py import Scratch2Py
print('Please enter your Scratch credentials below:')
username = input('  Username: ')
password = input('  Password: ')
s2py = Scratch2Py(username, password) 
usernameinput = input('Input Username Query: ')
while 1:
    user = s2py.user(usernameinput)
    if user.exists() != 'True':
        print(usernameinput + ' is not a valid username. Please type in a new user below.')
        usernameinput = input('Input Username Query: ')
    userinput = input('What info about ' + usernameinput + ' would you like to know? ')
    if userinput == 'quit':
        break
    if userinput == 'getMessagesCount()':
        print(user.getMessagesCount())
    if userinput == 'getMessages()':
        print(user.getMessages())
    if userinput == 'getStatus()':
        print(user.getStatus())
    if userinput == 'getBio()':
        print(user.getBio())
    if userinput == 'getProjects()':
        print(user.getProjects())
        
