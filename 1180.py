def menor(n, x1: list):
    if (x1[0]) < (x1[1]):
        menorN = (x1[0])
        d = 0
    else:
        menorN = (x1[1])
        d = 1
    p = 2
    
    for i in range(n-2):        
        if menorN < (x1[p]):
            menorN = menorN
                       
        else:
            menorN = (x1[p])
            d = p
        p += 1
    
    print(f"Menor valor: {menorN}")
    print(f"Posicao: {d}")
  
def main():
    n = int(input())
    x1 = list(map(int, input().split()))
    menor(n, x1)

main()
