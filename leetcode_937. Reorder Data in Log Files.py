#문제가 이해 덜 됨,,ㅠㅠ
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        start=0
        last=len(logs)-1
        while(start<last):
            s_prefix=ord(logs[start].split()[1][0])
            l_prefix=ord(logs[last].split()[1][0])
            if(s_prefix-ord('a')>=0):
                start+=1
                continue
            elif(l_prefix-ord('a')<0):
                last-=1
                continue
            temp=logs[start]
            logs[start]=logs[last]
            logs[last]=temp
            start+=1
            last-=1
        print(start)
        logs[:start]=sorted(logs[:start],key=lambda x: (x.split()[1:], x.split()[0]))
        logs[start:]=sorted(logs[start:])
        return logs
