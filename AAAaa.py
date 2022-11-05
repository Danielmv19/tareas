def uno():
    divisores = []
    n = int(input("escriba un numero: "))
    for divisor in range(1, n + 1):
        if (n % divisor) == 0:
            divisores.append(divisor)
    print("divisores de ", n )
    print(divisores)
uno()