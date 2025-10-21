def hanoi(n, i, j):
    if (n > 1):
        hanoi(n - 1, i, 6 - i - j)
        hanoi(1, i, j)
        hanoi(n - 1, 6 - i - j, j)
    else:
       print(f'Mover disco de {i} a {j}')

hanoi(3, 1, 3)