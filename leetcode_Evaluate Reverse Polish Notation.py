class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers=[]
        operators=['+','-','*','/']
        for token in tokens:
            if(token in operators):
                a=numbers.pop()
                b=numbers.pop()
                
                if(token=='+'):
                    numbers.append(b+a)
                elif(token=='-'):
                    numbers.append(b-a)
                elif(token=='*'):
                    numbers.append(b*a)
                else:
                    if((b//a)<0):
                        numbers.append(-(abs(b)//abs(a)))
                        
                    else:
                        numbers.append(b//a)

            else:
                numbers.append(int(token))
        
        return numbers.pop()
