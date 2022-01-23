#Przygotować skrypt, który pyta uzytkownika o dane personalne osoby
#(np imie, nazywsko, tel) i zapisuje je do JSONa. Obsłużyc wyjątek(Try/except)
#gdy podany nr tel nie jest prawdziwym nr tel.
#Przykładowe nr tel:(123-456-789, 123 456 789, 123456789)

import json
import re

pattern = "\d{3}\-?\ ?\d{3}\-?\ ?\d{3}"
numerTelefonu = input("wprowadz numer telefonu: ")
imie = input("podaj imie: ")
nazywsko = input("podaj nazwisko: ")

dict = { 
    "imie": imie,
    "nazywsko": nazywsko,
    "Numer Telefonu": numerTelefonu
}
try:
    if re.search(pattern, numerTelefonu):
        jsonDict = json.dumps(dict)
        f = open("new_json.json", "a")
        f.write("{0} \n".format(jsonDict))
        f.close()
    else:
        raise ValueError
except ValueError:        
    print("podany numer jest nieprawidłowy")

