#carmicheal number


num=int(input())
count=0
for i in range (2,num//2+1):
    if num%i==0:
        for j in range (2,10):
            if (j**num)%num==j:
                count+=1
        break
if count>5:
    print("the number", num ,"is a Carmichael number.")
else:
    print(num,"is normal")