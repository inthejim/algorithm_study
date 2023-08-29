class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        s=s.split()
        if(not s):
            return 0
        s=s[0]
        check=0
        k=0
        minus=False
        for i in range(len(s)):
            if i==k and (s[i]=='-' or s[i]=='+'):
                k+=1
                if(s[i]=='-'):
                    minus=not minus
                if(k%2==0 and minus==True):
                    return 0
                if(len(s)==k):
                    return 0
                continue
            if s[i]=='.':
                check=1
                if(check>1):
                    return 0
                continue
            if '0'>s[i] or s[i]>'9':   
                return 0
         
        # for i in range(len(s)):
        #     check=0
        #     for j in range(len(s[i])):
        #         if j==0 and s[i][j]=='-' or s[i][j]=='+':
        #             check=1
        #             continue
        #         if '0'>s[i][j] or s[i][j]>'9':     
        #             check=0       
        #             break
        #         else:
        #             check=1
        #     if not check:
        #         continue
        #     else:
        #         s=s[i]
        #         break
        s=s[k:]
        if check:
            s=float(s)
        
        s=int(s)
        if(minus):
            s=-s
        print(s)
        if(s<-(2<<31)+1):
            s=-(2<<31)+1
        elif(s>(2<<31-2)):
            s=(2<<31-2)
        return s
