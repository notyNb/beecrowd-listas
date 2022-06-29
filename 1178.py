def vetor(x):
    for i in range(100):
        print(f"N[{i}] = {x:.4f}")
        x = x / 2


def main():
    x = float(input())
    vetor(x)


main()
