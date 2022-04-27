def bsearchID(tplst,start,end,targetID):
    if start>end:
        return -1
    mid=(start+end)//2
    if tplst[mid][0]==targetID:
        return mid
    if tplst[mid][0]<targetID:
        return bsearchID(tplst,mid+1,end,targetID)
    else:
        return bsearchID(tplst,start,mid-1,targetID)
        
def binarySearchID(tplst,targetID):
    return bsearchID(tplst,0,len(tplst)-1,targetID)
    
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
