#------------------------
#generate random password
#------------------------

import string
import random

small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&@.,*()`+;:"

string = small + big + numbers + symbols
length = 32
password = "".join(random.sample(string,length))

print("password:" + password)

#made by BUCCI
