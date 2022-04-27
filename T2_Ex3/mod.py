def sortTupleList(tplst,k):
    L=len(tplst)
    for start in range(0,L-1):
        Min=tplst[start][k]
        min_idx=start
        for i in range(start+1,L):
            if tplst[i][k]<Min:
                Min=tplst[i][k]
                min_idx=i
        tplst[start],tplst[min_idx]=tplst[min_idx],tplst[start]
    return tplst
def prettyPrint(tpdata):
    list(tpdata)
    return "ID = "+ str(tpdata[0])+", Age = "+str(tpdata[1])+", Height = "+str(tpdata[2])
