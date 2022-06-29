#Smith Number

def smithNumber(n):
    i=2
    temp=n
    lst=[]
    while n>1:
        if n%i==0:
            lst.append(i)
            n=n/i
        else:
            i+=1

    count=0
    for j in lst:
        for k in range (2,(j//2)+1):
            if j%k==0:
                pass
        else:
            if j<10:
                count+=j
            else:
                while (j>0):
                    count+=j%10
                    j=j//10
    count1=0
    while (temp>0):
        count1+=temp%10
        temp=temp//10
        
               
    if count1==count:
        return True
    else:
        return False
    
    
n=int(input())
while (smithNumber(n) is not True):
    n+=1
print(n)
    

