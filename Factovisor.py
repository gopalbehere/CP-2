#Factovisor


i=int(input())
n=int(input())
a=n
facto=1
while (n>1):
    facto*=n
    n-=1
if facto%i==0:
    print(i," divides " , a , "!")
else:
    print(i," does not devides ", a , "!")

