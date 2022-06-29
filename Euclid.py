#Euclid problem


A=int(input(""))
B=int(input(""))


mm=mini=min(A,B)
maxi=max(A,B)
while(mini>1):
    if A%mini==0 and B%mini==0:
        gcd=mini
        break
        
    mini-=1
for i in range (0,-maxi,-1):
    for j in range (0,mm):
        if mm*i+maxi*j==gcd:
            print(i,j,gcd)
            break
    if mm*i+maxi*j==gcd:
        break

