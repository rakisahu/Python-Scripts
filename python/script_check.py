## Here we are trying to open files with different ways and getting some errors.
## our motive how to handle those exception errors with try: and except:
import os   #here just we used this OS module to pass a command clear, to clear the window, its not mendotary.
os.system("clear")
#open("abc.txt") #FileNotFoundError
#open("testosmodule.txt")    #PermissionError
try:
    open("/etc")    #PermissionError
except Exception as e:
    print(e)
filename= "/etc/hosts"
if os.path.exists(filename) and os.path.isfile(filename):
    print("file exists")
else:
    print("file doesn't exist, check spelling of filename or it could be a directory")

#print(os.path.exists("/etc/hosts")) # already discussed in practice.py
