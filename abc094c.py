'''
l is odd number, the median of numbers a1, a2,a3,...,al is the (l+1)/2-th largest value
N is even number, the median of numbers x1,x2,...,xi-1, xi+1, ...xn is bi

'''
n = int(input())
a = list(map(int, input().split(' ')))
i = 0
for i in range(n):
    ai = a[0:i] + a[i+1:n]
    aisrt = sorted(ai)
    l = int(len(aisrt)/2)
    
    print(aisrt[l])

#このコードはatcoderではTLEが出る
#forの中でソートをすると間に合わない
  
