# Part 1 - wait length (single trial)
import random
target_value1=int(input("Target value (1-1000)?"))
while target_value1>1000 or target_value1<1:
    target_value1=int(input("Target value (1-1000)?"))
    if target_value1<=1000:
        break
n=random.randint(1,1000)
waiting_length=0
while target_value1!=n:
    waiting_length+=1
    n=random.randint(1,1000)
print("Waiting length is "+str(waiting_length))


# Part 2 - max and min wait length (10000 trials)
import random
target_value2=int(input("Target value (1-1000)?"))
while target_value2>1000 or target_value2<1:
    target_value2=int(input("Target value (1-1000)?"))
    if target_value2<=1000:
        break
m=random.randint(1,1000)
Max=0
wait_length=0
trial_counter=0
waitlist=[]
while trial_counter<=9999:
    while target_value2!=m:
        wait_length+=1
        m=random.randint(1,1000)
    final=wait_length
    waitlist.append(final)
    if wait_length>Max:
        Max=wait_length
    wait_length=0
    m=random.randint(1,1000)
    trial_counter+=1

print("maximum waiting length is "+str(Max))
Min=min(waitlist)
print("minimum waiting length is "+str(Min))
