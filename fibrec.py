def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
num=int(input("enter no of terms:"))
print("fibonacci series:")
for i in range(num):
    print(fib(i),end=" ")
    
