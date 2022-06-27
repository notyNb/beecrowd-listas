def preenche(n: list):

    for i in range(1, 10):
        n.append(2 * n[i-1])

#==========================

def imprimir(n: list):
    for i in range(len(n)):
        print(f"N[{i}] = {n[i]}")

#===========================

def main():
    v = int(input())


    n = []
    n.append(v)

    preenche(n)

    imprimir(n)
    
    
main()
