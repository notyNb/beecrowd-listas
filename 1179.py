def preencher(par: list, impar: list):
    for i in range(15):
        valores = int(input())
        t = valores
        if t // 2 + t // 2 == valores:
            par.append(valores)
        else:
            impar.append(valores)
        for i in range(5):
            if len(par) == 5:
                print(f"par[{i}] = {(par[i])}")
            elif len(impar) == 5:
                print(f"impar[{i}] = {(impar[i])}")
        if len(par) == 5:
            par.clear()
        elif len(impar) == 5:
            impar.clear()
    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")
    
    


def main():
    par = []
    impar = []

    preencher(par, impar)
    
    

main()
