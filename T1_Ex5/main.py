#Part 1 - remove duplicates
string=input("Give me a sentence: ")
char={}
for i in string:
    char[i]=1
    if char[i]>1:
        char.remove(i)
list_1=list(char.keys())
for j in list_1:
    print(j, end='')

print('\n')
# Part 2 - random sequence
from random import random
dict_1={}
counter=True
while counter==True:
    a=int(random()*100)+1
    if a in dict_1.keys():
        dict_1[a]+=1
        print(a, end=' ')
        if dict_1[a]==3:
            counter=False
            break
    else:
        dict_1[a]=1
        print(a,end=' ')
