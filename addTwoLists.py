'''
1). Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą elementy na tych samych indeksach.
Możesz przypuścić, że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis ‘Podane listy muszą być tej samej długości’
'''

def dodajListy(a,b):
    if len(a)==len(b):
        print([a + b for a, b in zip(a, b)])
    else:
        print("Podane listy muszą być tej samej długości")

dodajListy([1,2,3,4,5], [1,2,3,4,5]) # [2, 4, 6, 8, 10]
dodajListy([1,2,3,4,5], [1,2,3,4]) # Podane listy muszą być tej samej długości

