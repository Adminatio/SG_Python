#sum of the square of even no.
n=int(input("Enter n terms:"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i**2
        print("Sum of squares are:",sum)
