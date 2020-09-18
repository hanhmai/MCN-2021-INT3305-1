import math

def prob(n,p):
    return ((1-p)**(n-1))*p

def infoMeasure(n,p):
    return -math.log(prob(n,p),2)

def sumProb(N,p):
    '''
    Với p = 1/2
        N = 5 : sumProb = 0.96875
        N = 12 : sumProb = 0.999
        N = 1000 : sumProb ~ 1
    ==> Tổng xác suất của phân bố Geometric bằng 1
    '''
    sumProb = 0
    for i in range (1,N+1):
        sumProb += prob(i,p)
    return sumProb

def approxEntropy(N,p):
    '''
    Entropy = E[I(x)] = p(x).I(x)
    Với p = 1/2, N = 1000: entropy = 1.99
    '''
    entropy = 0
    for i in range(1,N+1):
        entropy += prob(i,p) * infoMeasure(i,p)
    return entropy

print(approxEntropy(1000, 1/2))
print(sumProb(5,1/2))
print(sumProb(12,1.2))
print(sumProb(1000,1/2))