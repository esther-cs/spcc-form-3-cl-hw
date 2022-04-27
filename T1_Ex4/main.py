T = [ 19.6, 18.7, 18.8, 20.1, 19.6, 19.6, 19.6, 18.2,
      18.3, 18.5, 18.8, 18.8, 13.5, 17.9, 19.7, 19.1,
      19, 19.3, 19.1, 18.7, 18.9, 19.7, 18.3, 18.6,
      18.1, 12.8, 19, 13.6, 16, 18.4, 19.6, 17.6,
      19.4, 19.7, 19.9, 19.2, 19.7, 18.6, 19.1]
counter=0
total=0
print("Total number of regions: "+str(len(T)))
for i in range(0,len(T)):
    if T[i]>18.5:
        counter+=1
counter=str(counter)
print("Number of regions with temperature above 18.5 degC: "+counter)
for i in range(0,len(T)):
    total+=T[i]
avg=str(round(total/len(T),2))
print("Average temperature: "+avg)
