n=int(input("Enter the no.:"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
    if(flag==0):
        print(n,"is a prime no.")
    else:
        print(n,"not a prime no.")
