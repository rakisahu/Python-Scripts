# To create a python script to search for a file and then search for a file with specific extension.
# 1.find like utility (directory, then file to search like below)
    #ls -l /etc/*.conf  # ls -l /var/log/*.log

#   1.
import os
for dirname, dirpath, filename in os.walk("/etc"):
    print(dirname)
    print(dirpath)
    for file in filename:
       if file == "sysctl.conf":
            print(os.path.join(dirname,file))


