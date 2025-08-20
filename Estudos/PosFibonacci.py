def PosFibonacci(num):
    
    a, b = 0, 1
    pos = 1

    while a < num:
        a, b = b, a + b
        pos += 1

    if a == num:
        return pos
    else:
        return -1

num = int(input("Digite um número:"))
pos = PosFibonacci(num)

if pos != -1:
    print(f"O número {num} está na posição {pos} da sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")