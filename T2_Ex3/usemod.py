import mod as mylib
f = open("userdata.txt", "r")
alldata = [tuple([int(i) for i in j.split(',')]) for j in f.read().split('\n') if len(j) > 0]
f.close()
mylib.sortTupleList(alldata,0)
print("The upper quartile User ID data is "+ mylib.prettyPrint(alldata[len(alldata)//4]))
mylib.sortTupleList(alldata,1)
print("The upper quartile Age data is "+ mylib.prettyPrint(alldata[len(alldata)//4]))
mylib.sortTupleList(alldata,2)
print("The upper quartile Height data is "+ mylib.prettyPrint(alldata[len(alldata)//4]))
