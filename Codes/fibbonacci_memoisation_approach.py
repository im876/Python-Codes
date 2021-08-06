F_n = {0:0 ,1:1} #declaring fibbonacci for value n = 0 & 1
def fibbonacci(n):
    if n in F_n.keys():
        return F_n[n]
    else:
        F_n[n] = fibbonacci(n-1) + fibbonacci(n-2)
        return F_n[n]

n = int(input())
print(fibbonacci(n))
