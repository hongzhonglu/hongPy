# this script can be run the common line
# Whenever the Python interpreter reads a source file, it does two things:

# it sets a few special variables like __name__, and then
# it executes all of the code found in the file.
# Let's see how this works and how it relates to your question about the __name__ checks we always see in Python scripts.

import sys

def myFunction(a,b):
    print("The sum result is:", int(a) + int(b))

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    myFunction(a,b)