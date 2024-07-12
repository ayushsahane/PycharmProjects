import random
import string
length=int(input("Enter length of password:"))
#length
chars=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.printable
#character to make password 
password=""
#store password
for c in range(length):#8, 0,1,2,---7
    password=password+password.join(random.sample(chars,1))
    print(password)
    print("Final password generated:", password)
    password_direct=""
    password_direct=password_direct.join(random.sample(chars,length))
    print("direct generated password is",password_direct)
