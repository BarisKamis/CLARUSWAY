sayilar=[]
for i in range(1,6):
    print ("bir sayi girin")
    x=input()
    sayilar.append(int(x))
    i=i+1

enbuyuk=sayilar[1]
for i in sayilar:
    if i > enbuyuk:
        enbuyuk=i
    i=i+1
print ("en buyuk sayi:", enbuyuk)