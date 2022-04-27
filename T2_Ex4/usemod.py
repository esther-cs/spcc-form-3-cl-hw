import mod as mylib
f = open("userdata.txt", "r")
alldata = [tuple([int(i) for i in j.split(',')]) for j in f.read().split('\n') if len(j) > 0]
f.close()
mylib.sortTupleList(alldata,0)
flag=True
while flag:
    userid=int(input("Enter User ID to search:"))
    if userid==0:
        print("Bye")
        break
    else:
        idx=mylib.binarySearchID(alldata,userid)
        if idx!=-1:
            print("User ID:",userid)
            print("Age:",alldata[idx][1])
            print("Height:",alldata[idx][2])
        else:
            print("Record not found")
