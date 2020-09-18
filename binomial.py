import math

def factorial(n)
    if n == 0:
        return 1
    else return n * factorial(n-1)

def prob(n,p,N)
    return factorial(N) / (factorial(n) * factorial(N-n)) * (p**n) * (1-p)**(N-n)

def infoMeasure(n,p,N)
    return -math.log(prob(n,p,N),2)

def sumProb(N,p):
    '''
    Tổng xác suất của các symbol n với n chạy từ 1 đến N
    '''
    sumProb = 0
    for i in range (1,N+1):
        sumProb += prob(i,p,N)
    return sumProb

def approxEntropy(N,p):
    '''
    Entropy của nguồn tin có phân bố xác suất Binomial
    '''
    entropy = 0
    for i in range(1,N+1):
        entropy += prob(i,p,N) * infoMeasure(i,p,N)
    return entropy

