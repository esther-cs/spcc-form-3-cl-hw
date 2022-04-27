#Part 1 - Factorial
n=int(input("n = ? "))
total=1 
for i in range(1,n+1):
    total=total*i
n=str(n)
total=str(total)
print("The factorial of "+n+" is "+total)

#Part 2 - do some stat
print("Please enter 10 positive integers (enter -ve values to stop immediately).")
counter=0
total=0
for i in range(10):
    n=int(input("number? "))
    if n>0:
        counter+=1
        total=total+n
    elif n<0:
        break
length=str(counter)
average=str(total/counter)
print("You have entered "+length+" positive integers")
print("The average is "+average)
