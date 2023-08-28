class Solution:
    def reverse(self, x: int) -> int:
        k=str(x)
        s=""
        last=-1
        if(k[0]=='-'):
            s+='-'
            last=0
        for i in range(len(k)-1, last, -1):
            s+=k[i]
       
        i=0
        while(i<len(s)):
            if(s[i]=='0'):
                s=s[i:]
                i+=1
            else:
                break
                
        s=int(s)
        #왜 숫자범위를 -2<<31로 하면 안되는지,,
        if(s<=(-2<<30) or s>=(2<<(31)-1)):
            return 0
        return int(s)
                
                
