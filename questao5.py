n = int(input())

h = 1
s = 1
p = 2

primo = 3

for i in range(2, n+1):
    print(primo)
            
    if i % 2 == 0:
        h += (i*2 - 1)/i
        s -= i/i**2
    else:
        h -= (i*2 - 1)/i
        s += i/i**2
    
    p = primo/(2*i - 1)**3

    eh_primo = False
    while not eh_primo:
        primo = primo + 1
        eh_primo = True
        for j in range(2, int(primo/2)+1):
            if primo % j == 0:
                eh_primo = False
                break

print(h)
print(s)
print(p)