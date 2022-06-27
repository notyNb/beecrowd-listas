def imprimir(n: list):
    for i in range(len(n)):
        print(f"N[{i}] = {n[i]}")



#========================

def main():
    n = []
    for i in range(20):
        v = int(input())
        n.insert(0, v)

    
    imprimir(n)

main()
