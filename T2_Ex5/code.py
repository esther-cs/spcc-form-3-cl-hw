class Staff:
  def __init__(self,id,name,sex,height,waist):
    self.id=id
    self.name=name
    self.sex=sex
    self.height=height
    self.waist=waist
  def __str__(self):
      return f"ID: {self.id}\nName: {self.name}\nSex: {self.sex}\nHeight: {self.height}\nWaist: {self.waist}"
  def rfm(self):
      if self.sex=="M":
          return 64-20*(self.height/self.waist)
      else:
          return 76-20*(self.height/self.waist)
def readStaffData(fname):
    lst = []
    f = open("bodysizes.txt", "r")
    for j in f.read().split('\n'):
        if len(j) > 0:
            items = j.split(',')
            items[3] = float(items[3])
            items[4] = float(items[4])
            lst.append( Staff( *items ) )
    f.close()
    return lst
alldata = readStaffData("bodysizes.txt")
counter_m=0
counter_f=0
max_m=0
max_f=0
for i in range(len(alldata)):
    if alldata[i].rfm()>22.8 and alldata[i].sex=="M":
        counter_m+=1
    elif alldata[i].rfm()>33.9 and alldata[i].sex=="F":
        counter_f+=1
    if alldata[i].rfm()>alldata[max_m].rfm() and alldata[i].sex=="M":
        max_m=i
    elif alldata[i].rfm()>alldata[max_f].rfm() and alldata[i].sex=="F":
        max_f=i
print("No. of male exceeding RFM healthy limit: "+str(counter_m)+"\nNo.of female excedding RFM healthy limit:"+str(counter_f)+"\n")
print("Male with highest RFM: (="+str(alldata[max_m].rfm())+")")
print(alldata[max_m])
print("\nFemale with highest RFM: (="+str(alldata[max_f].rfm())+")")
print(alldata[max_f])







