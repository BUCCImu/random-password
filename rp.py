import string
import random

small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&@.,*()`+;:"


string = small + big + numbers + symbols
length = random.randrange(20, 30)
password = "".join(random.sample(string,length))

print("Password: " + password)

n = input("File Name: ")

f = open(n + ".txt", 'x')
f.write(password)
f.close()