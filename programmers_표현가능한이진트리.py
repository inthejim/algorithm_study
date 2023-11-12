def search(number) :
    length = len(number)
    if length == 1 or ('1' or '0') not in number:
        return True
    
    root = length // 2
    if number[root] == '0':
        return False
    
    return search(number[:root]) and search(number[root+1:])

def solution(numbers):
    #bin: 내장함수, 정수를 이진수 문자열로 변환, '0bxxxx'형태
    bin_numbers = [ bin(number)[2:] for number in numbers]
    bin_list = [ 2**x - 1 for x in range(50)]
    answer = list()
    for number in bin_numbers :
        print(number)
        length = len(number)
        for num in bin_list :
            print(num)
            if num >= length :
                number = '0'*(num-length) + number
                break
        answer.append(1 if search(number) else 0)
    
    return answer
