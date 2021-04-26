"""
CTRL + SHIFT + D --> VSC, Run and Debug
Funkcja will_weapon_hit zwraca wartości typu string
String - tablica typu char
czy ktoś trafił.
Czyli 50% szansy, to jeżeli wylosowana liczba od 0 do 100
jest mniejsza od 50, to hit.



while x < 5:
    x = x + 1
    listHit.append(will_weapon_hit(50))
Takie losowanie przebiega 5 razy.


Gdyby było 100% szansy na trafienie, to jeżeli wylosowana
liczba z zakresu 0 - 100 jest mniejsza od 100, czyli zawsze
trafia.



Zapisanie wyniku zwracanego przez funkcję od razu do 
listy:
listHit.append(will_weapon_hit(50))


Po lewej należy zaznaczyć breakpoint aby wskazać debugerowi, gdzie
przerwać wykonywanie kodu.


W zakładce variables są widoczne teraz zmienne, funkcje itd. 
lokalne oraz globalne.
Są tam widoczne także zaimportowane moduły.
Są także widoczne rzeczy istniejące w zaimportowanym module.

Przyciski w górnym panelu podczas debugowania:
Step Over - debuger pozwoli na wykonanie jednej instrukcji więcej.
Lista w programie widoczna w panelu Variables jako oddzielna gałąź.

Wszelkie zmiany zachodzące w takiej liście są na bieżąco aktualizowane
w panelu Variables debugera.
Wartości zmiennych także są widoczne i aktualizowane na bieżąco.

Step Into - przejście do środka wykonywanej funkcji.
W takiej sytuacji zmienne globalne i lokalne zostają wyświetlone, 
ale z perspektywy tej funkcji, bo wcześniej były wyświetlone względem
całego programu a nie pojedynczej funkcji.


Continue - przeskakuje pomiędzy wieloma ustalonymi przez 
użytkownika breakpoint'ami. Jeżeli jest tylko jeden, debuger
pozwoli na wykonanie się programu do końca.


Restart - restart od początku debugowania, jeżeli chcemy zacząć
od nowa.


Stop - zakończenie.


Step Out - Debuger wychodzi z jakiejś funkcji, w której teraz się
znajduje i analogicznie jak w Step Into, zostają wyświelone teraz
zmienne lokalne i globalne z perspektywy całego programu a nie 
tylko tej funkcji.
Dopóki jesteśmy wewnątrz funkcji will_weapon_hit, jest widoczny
isHitChance z obliczoną szansą, np. 79.21383...
Z perspektywy tej funkcji jest to zmienna lokalna i tak jest 
widoczna w panelu Variables.
===============================================================

Można po zaznaczeniu breakpoint, kliknąć PPM na niego i wybrać
Edit Breakpoint a następnie Log Message. Taki 'komentarz' będzie
niewidoczny bezpośrednio w kodzie.
Komentarze widoczne dla nas do debugowania w przyszłości.
Można zamiast Log Message wybrać Hit Count, czyli np. wpiszemy 2, 
to breakpoint zostanie wywołany dopiero, gdy program podczas 
wykonywania się natrafi na niego drugi raz.
===============================================================

[Variables] Call Stack - kolejność wywoływania funkcji na stosie
funkcji w kodzie.
Sterta/Stos:
Na stercie pamięć jest alokowana gdzie tylko się da, czyli zasięganie
do takich danych będzie szybsze, w przypadku stosu dane są 
uporządkowane i żeby dostać się do danych umieszczonych jako 
pierwsze w stosie, trzeba przedostać się poprzez wszystkie dane 
je poprzedzające.
Można to porównać trochę do logiki szybkości działania zbioru i 
listy. W liście dane są uporządkowane i zajmuje stosunkowo sporo
miejsca w pamięci w związku ze swoją funkcjonalnością na danych, natomiast
zbiór umieszcza dane losowo, więc dostęp do nich będzie ciut szybszy i sam 
zbiór będzie zajmować trochę mniej miejsca w pamięci.
W przypadku zbiorów zyskujemy funkcjonalności niezbędne np. do 
porównywania dużej ilości danych pomiędzy serwerami (dane wspólne, lub czy
dane z serwera A są wszystkie w serwerze B [czy zbiór A jest podzbiorem zbioru B]),
czyli operacje na zbiorach, suma, różnica, części wspólne, podzbiór.

Do koniecznego przechowywania dużej ilości danych np. o userach krotki będą idealne.
Nie można danych edytować, dodawać, odejmować ich (danych), więc zajmują tylko tyle miejsca 
'na styk' w pamięci, ile potrzebują, w zamian tracimy właśnie tą funkcjonalność operowania
na danych.


Słowniki podobne w deklaracji do zbiorów, zawierają klucze i wartości do nich przypisane,
można różne obiekty przechowujące dane mieszać ze sobą, czyli np słownik krotek o userach,
gdzie każdy user ma ID (klucz w słowniku) natomiast dane o nim to wartość przypisana do 
takiego klucza i jest to krotka.
Takie obiekty można zagnieżdżać w sobie dowolnie dużo.
Ale żeby miało to sens jeżeli chodzi o optymalizacje i użyteczność w kodzie.
Słownik ma tą cechę, że można najszybciej ze wszystkich możliwości odnaleźć dane, po 
kluczu, nie trzeba używać do tego pętli przechodzącej przez cały obiekt.



Generatory są najlepszym wyborem do operowania na wielo terabajtowych danych, żeby 
nie trzeba było przechowywać ich w pamięci, ale nie możemy operować na danych wcześniej
wygenerowanych, mamy dostęp tylko do n- elementu, natomiast do n-1 i aż do n-ilość_
elementów_do_tej_pory nie mamy dostępu.
Generator będzie generował dane w oparciu o jakiś pattern, wzór np w takim pliku.
Generator będzie zawsze zajmował tak samo mało miejsca bez względu na to, z jak 
dużej ilości danych generuje elementy.

======================================================================================
Call stack może być użyty do sprawdzenia np. jak zachowuje się funkcja 
dopiero po np. 30 wywołaniu jej.

======================================================================================

Zaznaczenie breakpoint, PPM na niego, Edit, Expression i można 
wywołać breakpoint dopiero, gdy np. jakaś zmienna osiągnie określoną
wartość, np. wpisać tam weaponChanceToHitPercentage == 50


Log Message nie wpływa na wywoływanie się breakpointów.


======================================================
Zakładka Watch pod Variables.
służy do podglądu zmiennej, funkcji itp. w sposób ciągły, bez 
przerwy mamy podgląd na to, co tam wpiszemy po użyciu plusa,
na wartości tam przechowywane na bieżąco itd.
Do wartości podglądanych w Watch mamy dostęp niezależnie, z jakiej
perspektywy korzystamy z debugera (z środka funkcji, z globalnej
dla pliku itd.).
======================================================

Interakcja z userem nie wpłynie na przerwanie się pracy debugera 
(np. input).


int(input("Podaj szanse na uderzenie broni"))
Rzutowanie wprowadzonych danych od razu do typu int.
i teraz zaznaczenie breakpoint i np. Expression, gdy 
weaponHitPercentage == 40, czyli co się dzieje w programie, gdy
user poda specyficzną wartość dla funcji.
=======================================================

Jeżeli zależy nam na wejściu do funkcji importowanej z
zewnętrznego modułu bądź z modułu przygotowanego przez 
developerów, np. uniform, należy w pliku launch.json dopisać
w liście słowników configurations następujący klucz:wartość :
"justMyCode": false
Zmiana pracy debugera, że 'nie tylko mój kod'.

Teraz można podglądać też jak taki np. uniform 
został przez kogoś napisany w pliku random.py

W Call Stack widać kolejność wywoływanych funkcji, metod itd.
z zewnętrznego pliku, tutaj random.py
=======================================================
"""
from collections import Counter
import random


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)

    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"


x = 0

listHit = []
weaponHitPercentage = int(input("Podaj szanse na uderzenie broni"))
while x < 5:
    x = x + 1
    listHit.append(will_weapon_hit(weaponHitPercentage))


dictionaryHit = Counter(listHit)

print(listHit)