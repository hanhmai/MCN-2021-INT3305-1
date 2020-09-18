import math

def factorial(n)
    if n == 0:
        return 1
    else return n * factorial(n-1)

def prob(n,p,r)
    return factorial(n)/(factorial(n-r+1)*factorial(r-1)) * (p**r) * (1-p)**(n-r)

def infoMeasure(n,p,r)
    return -math.log(prob(n,p,r),2)

def sumProb(N,p,r):
    '''
    Tổng xác suất của các symbol n với n chạy từ 1 đến N
    '''
    sumProb = 0
    for i in range (1,N+1):
        sumProb += prob(i,p,r)
    return sumProb

def approxEntropy(N,p,r):
    '''
    Entropy của nguồn tin có phân bố xác suất Negative Binomial
    '''
    entropy = 0
    for i in range(1,N+1):
        entropy += prob(i,p,r) * infoMeasure(i,p,r)
    return entropy



