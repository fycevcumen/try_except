#hatalar / ististnalar (exceptions)
#ZeroDivisionErrork
#01
a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print('Payda da sifir olmaz') 
    
#tip hatası
#02
a = 10
b='2'

try:
    print(a/b)   
except TypeError:
    print('Sayı ve str problemi')
#03
a = 10
b=2
try:
    print(a/b)
except TypeError:
    print('Sayı ve str problemi')
#problemleri çözmeye çalışmak en önemli tavsiyedir...