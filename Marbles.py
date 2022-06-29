#Marbles


def marbles(n,n1,c1,n2,c2):
    
    a=c1/n1
    b=c2/n2
    if (a<b):
        for i in range (n//n2+1):
            for j in range (1,n//n1+1):
                if (n2*i)+(n1*j)==n:
                    return (i,j)
                    
        
        else:
            return ("failed")
    else:
        for i in range (n//n1+1):
            for j in range (1,n//n2+1):
                if (n1*i)+(n2*j)==n:
                    return j,i
                       
        else:
            return ("failed")

n=int(input("enter the no. marbles to buy"))
n1=int(input())
c1=int(input())
n2=int(input())
c2=int(input())
print(marbles(n,n1,c1,n2,c2))
