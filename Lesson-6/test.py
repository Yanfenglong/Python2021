def is_odd(n):
    return n%2 ==1
def fun(a,b,c):
    return a+b+c
def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

    #ctrl+S