modal = 100000000
laba = 0
Total_laba = 0
for i in range(1, 9):
    if i <= 2:
        laba = 0
        Total_laba = Total_laba + laba
        print("laba bulan ke-", i, "sebesar :", laba)
    elif i <= 4:
        laba = modal * 1 / 100
        Total_laba = Total_laba + laba
        print("laba bulan ke-", i, "sebesar :", laba)
    elif i <= 7:
        laba = modal * 5 / 100
        Total_laba = Total_laba + laba
        print("laba bulan ke-", i, "sebesar :", laba)
    elif i <= 8:
        laba  = modal * 3 / 100
        Total_laba = Total_laba + laba
        print("laba bulan ke-", i, "sebesar :", laba)
print("Total laba adalah: ",Total_laba)
