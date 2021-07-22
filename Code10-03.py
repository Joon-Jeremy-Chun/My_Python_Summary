#반복문 구현

#1부터10까지 합계를 구하는 예
sumValue = 0
for n in range(10,0,-1) :
    sumValue += n
print(sumValue)

#1부터 numb까지 합계를 구하는 예
def addNumber(numb) :
    if numb <= 1 :
        return 1
    return numb + addNumber(numb-1)

print(addNumber(20))
