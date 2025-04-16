def Merge(l1,s,m,e):
    i=s
    j=m+1
    
    ans=[]
    
    while(i<=m and j<=e):
        if(l1[i]<l1[j]):
            ans.append(l1[i])
            i+=1
        elif(l1[i]>l1[j]):
            ans.append(l1[j])
            j+=1
        elif(l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i+=1
            j+=1
            
    while(i<=m):
        ans.append(l1[i])
        i+=1
    while(j<=e):
        ans.append(l1[j])
        j+=1
    
    startmyans=0
    startmylist=s
    while(startmylist<=e):
        l1[startmylist]=ans[startmyans]
        startmyans+=1
        startmylist+=1
    return

def Mergesorthelper(l1,s,e):
    if(s>=e):
        return
    
    m=s+(e-s)//2
    
    Mergesorthelper(l1,s,m)
    Mergesorthelper(l1,m+1,e)
    
    Merge(l1,s,m,e)
    return

def Mergesort(l1):
    return Mergesorthelper(l1,0,len(l1)-1)
    

l1=[4,3,6,2,4,1,10]
Mergesort(l1)
print(l1)