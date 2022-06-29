#Honoi Tower

pegs=int(input("enter no of pegs"))
lst=[]
matrix=[]

for i in range(1,pegs+1):
    lst.append(i*i)
    matrix.append([0])

j=1
while (j<lst[-1]):
    for i in range (len(matrix)):
        if matrix[i]==[0]:
            matrix[i].append(j)
            j+=1
            break
        if ((matrix[i])[-1]+j) in lst:
            matrix[i].append(j)
            j+=1
            break
    else:
        print(j-1)
        break

    


