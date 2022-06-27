#===================

def imprimir(a, o: list):
    p = 0
    for i in range(len(a)):
        print(f"Fib({(o[p])}) = {a[i]}")
        p += 1

#===================
def main():
    n = int(input())
    a = []
    o = []
    for i in range(n):
        v = int(input())
        a.append(v)
        o.append(v)

    p = 0
    for i in range(len(a)):
        b = 0
        c = 1
        f = 0
        k = 0
        if a[p] == 0:
            k+=1
        else:
            for i in range(0, a[p]):                    
                f = b + c
                c = b
                b = f
        a[p] = f
        p += 1
    
    imprimir(a, o)
  

main()
