#summation of four primes



num=int(input())
i=2
lst=[]
while(i<num):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        lst.append(i)
    i+=1
if num%2==0:
    l2=num-4
    for m in lst:
        for p in lst:
            if m+p==l2:
                print(2,2,m,p)
                break
        if m+p==l2:
            break
    else:
        print("impossible!")
    
    
    
else:
    l2=num-5
    for m in lst:
        for p in lst:
            if m+p==l2:
                print(2,3,m,p)
                break
        if m+p==l2:
            break
    else:
        print("impossible!")

        
