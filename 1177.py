def listaT(t, n: list):
    p = 0
    for i in range(1000):
        if p < t:
            n.append(p)
            p += 1
        else:
            p = 0
            n.append(p)
            p += 1
    

def imprimir(n):
    p = 0
    u = []
    for i in range(1000):
        print(f"N[{i}] = {n[p]}")  
        p += 1


def main():
    n = []
    t = int(input())

    listaT(t, n)
    imprimir(n)

main()
