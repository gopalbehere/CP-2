#Light more light

while True:
    bulbs=int(input())
    if bulbs==0:
        break
    for i in range (bulbs//2+1):
        if i*i==bulbs:
            print("Yes")
            break
    else:
        print("No")



