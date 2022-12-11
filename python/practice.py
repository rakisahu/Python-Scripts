import os
os.system("clear")
##os.system("pwd")
#os.system("ls -ltr")
#os.system("mkdir testosmodule1")
#os.system("touch testosmodule1.txt")
#os.system("ls -ltr")
#os.getcwd()
#os.listdir()     
        ##os.listdir("/path")
#os.chdir("/tmp")                ## to change to another directory
                ##os.chdir("/path") ## always required a path argument
#os.mknod("testfileforomknod1sd112")   ## To create a file
#os.mkdir("Example12")             ## To create a Directory
#os.makedirs("Exampless1/example1ss1") ## To create a Directory inside a directory
#os.system("ls -ltr")
#os.chdir("/tmp")
#os.rename("testfileforomknod1sd112","myfile1aa1")
#os.system("ls -ltr") ##
#os.path()       ## Submodule of os module 
## os.path.exists("/path") ## always required a path argument
x = os.path.exists("/home/raki/devops")
y = os.path.exists("/home/raki/practice")
print(x, "it exist")
print(y, "it doen't exist")
# os.path.isfile("/Path required") ## to check whether a file exist with the given name or not always required a path argument
## Result either only can be True/False, so here to print output of below result x and y used as a variable, which will store the result and print.
x=os.path.isfile("/home/raki/devops")
y=os.path.isfile("/home/raki/devops/practice/python/first.py")
print(x,"file")
print(y,"file")
# os.path.isdir("/Path required")    ## to check whether a file exist with the given name or not, required a path.
## Result either only can be True/False, so here to print output of below result x and y used as a variable, which will store the result and print.
x=os.path.isdir("/home/raki/devops")
y=os.path.isdir("/home/raki/devops/practice/python/first.py")
print(x,"dir")
print(y,"dir")
#os.path.islink("/Path required")    ## to check whether a file or directory having a symbolic link or not, required a path.
## Result either only can be True/False, so here to print output of below result x and y used as a variable, which will store the result and print.
x=os.path.islink("/etc")
y=os.path.islink("/etc/vtrgb")
print(x,"Link")
print(y,"Link")
#os.path.getsize("/Path required")      ## To check the size(in KB) of file in filesystem.
x=os.path.getsize("/home/raki/devops/practice/python/practice.py")
print("file size is", x)
#os.path.basename("/Path required") ## To check the basename of dir or file
x=os.path.basename("/home/raki")
print("basename is", x, "and its always", (y==os.path.isdir("/home/raki")))        # Just print the result in a better readable format here y variable used with == and called isdir submodule here
#os.path.dirname("/Path required") ## To check the dir name in given path.
x=os.path.dirname("/home/raki")
print("dir is ",x)
#os.path.join("/Path required")
os.path.join("/home/raki/devops/practice/python/","joinfile")
os.system("pwd")
os.system("ls -ltr")
#os.walk("/Path required to see the details inside") # it will list all the directories and files inside the directory like all details)
## Basically waht os.walk perform
## dirpath
## dirname
## filename
#print(list(os.walk("/tmp/walktest")))
for dirpath,dirname,filename in os.walk("/tmp/walktest"):
        print(dirpath)
        print(dirname)
        for file in filename:
                print(os.path.join("filename",file))