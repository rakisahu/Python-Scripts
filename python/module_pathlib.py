## Here we imported pathlib module to check a file is exist, its a file or a directory in different ways
## by using exists,is_file and is_dir options

import pathlib

a = pathlib.Path("/etc/hosts")
print(a)
print(a.exists())
print(a.is_file())
print(a.is_dir())

