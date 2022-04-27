f=open("userdata.txt","r")
alldata=[tuple([int(i) for i in j.split(',')]) for j in f.read().split('\n') if len(j)>0]
f.close()
for x in alldata:
    n=len(x)
    break
list_1=[]
counter=0
while counter<n:
    for i in range(len(alldata)):
        min_idx=i
        for j in range(i+1,len(alldata)):
            if alldata[j][counter]<alldata[min_idx][counter]:
                min_idx=j
        alldata[i],alldata[min_idx]=alldata[min_idx],alldata[i]
    median=alldata[len(alldata)//2][counter]
    list_1.append(median)
    counter+=1
print("The median User ID is", list_1[0])
print("The median Age is", list_1[1])
print("The median Height is", list_1[2])
