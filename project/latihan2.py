x = 0
while not x:
    n = int(input("Masukkan bilangan : "))
    if (n > 0):
        Terbesar = n
        continue
    elif (n < 0):
        continue
    else:
        break
print("Bilangan terbesar adalah : ",Terbesar)