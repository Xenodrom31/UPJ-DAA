def bilangan_prima():
    prima = []
    for i in range(1, 100):
        j = 1
        count = 0
        while j <= i:
            if i % j == 0:
                count += 1
            j += 1
        if count == 2:
            prima.append(i)
    return prima

def faktor_prima(x):
    faktor = {}
    primanya = bilangan_prima()
    for i in primanya:
        count = 0
        while x % i == 0:
            x = x / i
            count += 1
        if count != 0:
            faktor[i] = count
    return faktor

def eliminasi_prima(x, y):
    faktor = {}
    for i in x:
        terbesar = 0
        if i in y:
            if x[i] > y[i]:
                terbesar = x[i]
            elif x[i] < y[i]:
                terbesar = y[i]
            else:
                terbesar = x[i]
            
            faktor[i] = terbesar
        else:
            faktor[i] = x[i]
    for i in y:
        if i not in x:
            faktor[i] = y[i]
    return faktor

def kpk(x):
    hasil = 1
    for i in x:
        hasil = hasil * i ** x[i] 
    return hasil
        

x = 3
y = 4

faktor_prima_1 = faktor_prima(x)
faktor_prima_2 = faktor_prima(y)
print(faktor_prima_1, faktor_prima_2)
print(kpk(eliminasi_prima(faktor_prima_1, faktor_prima_2)))