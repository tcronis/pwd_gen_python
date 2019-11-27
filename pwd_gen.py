import random
import time

# collecting the max length of the password
max = input("Max length? ")
pwd = ''
special = ['!', '@', '#', '$', '%', '&']
random.seed(int(round(time.time() * 1000)))

for count in range(int(max)):
    type = random.randint(1,3)
    if type == 1:
	    pwd += chr(random.randint(65,90))
    elif type == 2:
	    pwd += chr(random.randint(97,122))
    else:
	    pwd += random.choice(special)
print(pwd)   
