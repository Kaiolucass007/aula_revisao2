a = 0
b = 1
cnt = 1

while cnt <= 20:
    print(f'Numero {cnt} da sequência sequencia: {a}')
    a,b = b, a + b
    cnt += 1
    