
def myfunction(*args, **kwargs):
    
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs["Keyone"])
    print(kwargs["Keytwo"])

myfunction('hey', True, 19, 'hello', Keyone = "World", Keytwo = 15)


import sys
# Usage: ArgumentParsing.py FILENAME
filename = sys.argv[1]
message = sys.argv[2]
with open(filename, 'w+') as f:
    f.write(message)

import getopt
import sys

filename2 = "hello.txt"
message = "This is Sparta"

opts, args = getopt.getopt(sys.argv[1:], "f:m:")

print(opts)
print(args)

for opt, arg in opts:
    if opts == '-f':
        filename = arg
    if opt == 'm':
        message = arg

with open (filename2, 'w+') as f:
    f.write(message)