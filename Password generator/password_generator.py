# password generation
import random
alpha = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9' ]

special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', 
    '-', '_'
]
password=[]
print("===welcome to password generator====")
nalpha=int(input("enter count of alphabets to be there in password : "))
nnum=int(input("enter  count of numbers  : "))
nspcl=int(input("enter count of  special characters : "))

for i in range(nalpha):
    password.append(random.choice(alpha))
for i in range(nnum):
    password.append(random.choice(numbers))  
for i in range(nspcl):
    password.append(random.choice(special_chars)) 
    

random.shuffle(password)
# print(password)
newpass=""
for char in password:
  newpass+= char
print(f"Password : {newpass} ")
