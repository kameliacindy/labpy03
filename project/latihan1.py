import random
a = input("Masukkan nilai N : ")
jumlah = 5
for i in range(jumlah):
    N = random.uniform(0, 0.5)
    print("data ke:", i+1, "=>", N)
print("Selesai")