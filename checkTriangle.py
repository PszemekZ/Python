'''
2). Stwórz funkcję nazwaną zbadajTrojkat() która przyjmie jako argumenty długości boków trójkąta.
Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, równoboczny, różnoboczny lub nieprawidłowy
'''

def zbadajTrojkat(a,b,c):
    if a**2 + b**2 == c**2:
        print("trójkąt prostokątny")
    elif (a==b or a==c or b==c) != (a == b == c):
        print("trójkąt równoramienny")
    elif a == b == c:
        print("trójkąt równoboczny")
    elif a != b and a != c and b != c:
        print("trójkąt różnoboczny")
    else:
        print("trójkąt nieprawidłowy")

zbadajTrojkat(3, 4, 5) #prostokątny
zbadajTrojkat(4, 5, 5) #równoramienny
zbadajTrojkat(5, 5, 5) #równoboczny
zbadajTrojkat(2, 5, 3) #różnoboczny
zbadajTrojkat(2, 5, 3, 5)
