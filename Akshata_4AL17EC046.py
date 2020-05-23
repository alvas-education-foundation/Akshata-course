t=0
while t<3:
i1=input("enter the username : ")
i2=input("enter the password : ")
if i1=='Micheal' and i2=='e3$WT89x':
print('Loggedin Successfully')
break
else :
print('Invalid username or password')
t+=1
if t==3:
print("Account Locked")