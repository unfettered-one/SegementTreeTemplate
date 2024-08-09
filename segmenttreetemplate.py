class SegmentTree:
    def __init__(self,n):
        self.seg=[None]*(4*n)
    
    def build(self,i,low,high,l):
        #Builing a segment tree (mininum segmet tree)
        if low==high:
            self.seg[i]=l[low]
            return
        m=(low+high)//2
        self.build(2*i+1,low,m,l)
        self.build(2*i+2,m+1,high,l)
        self.seg[i]= min(self.seg[2*i+1],self.seg[2*i+2])


    def query(self,i,l,r,low,high):
        #Using a segment tree to find the minimum for our interval low to high
        if r<low or l>high:
            return float('inf')
        if l>=low and r<=high:
            return self.seg[i]
        m=(l+r)//2
        a=self.query(2*i+1,l,m,low,high)
        b=self.query(2*i+2,m+1,r,low,high)
        return min(a,b)
        

    def update(self,ind,i,l,r,val):
        if l==r:
            self.seg[ind]=val
            return
        m=(l+r)//2
        if i<=m:
            self.update(2*ind+1,i,l,m,val)
        else:
            self.update(2*ind+2,i,m+1,r,val)
        self.seg[ind]=min(self.seg[2*ind+1],self.seg[2*ind+2])
        
l1=[1,3,2,0,4,5]
l2=[]
n1,n2=len(l1),len(l2)
seg1=SegmentTree(n1)
seg2=SegmentTree(n2)
seg1.build(0,0,n1-1,l1)
print(seg1.seg)

