"""
Tworzenie skrótów do komend, które nas interesują:
Np. po kliknięciu PPM w obszar roboczy nie ma przypisanego
skrótu do opcji:
Run Python File in Terminal
Jest też zielony przycisk Play po prawej stronie od zakładki otwartego
pliku.
CTRL + SHIFT + P --> open keyboard shortcuts 
CTRL + K, CTRL + S --> skróty do różnych instrukcji komend.
Szukamy: Run Python File in Terminal, potem szybko LPM i ustawiamy
skrót, np. CTRL + ALT + D
Podczas ustawiania skrótu, jeżeli spróbujemy przypisać istniejący już
skrót do czegoś, to otrzymamy informację zwrotną, że dany skrót 
już ma przypisane opcje do siebie i będzie można kliknąć w komunikat
i zobaczyć, do czego został już przypisany.
Jeżeli np. CTRL + W jest zajęte, to można zrobić przejście na kolejne:
CTRL + W chord to CTRL + W




Odpalenie programu w powłoce interaktywnej:
PPM na obszar roboczy --> Run Current File in Python Interactive Window
Zainstalować Jupyter'a
Możliwość podglądu kodu bezpośrednio w powłoce.
Możliwość podglądu zmiennych w pliku, ich typu, wartości,
ilości przechowywanych przez nie elementów (np. słownik).
Na dole jest niebieski obszar, w którym można wpisywać kod a następnie go 
wykonać przy pomocy SHIFT + ENTER.
Można tak wpisać np. nazwę zmiennej z pliku Python i wyświetlić jej wartość.
Można tak operować na tych zmiennych, np. dodać 100.
Czyli to jest taka 'symulacja' dla Python IDLE.
Można zmienne wyświetlane w okienku Variables zobaczyć w przyzwoitej formie
za pomocą opcji 'Show variable in data view', aby z niej skorzystać konieczne 
jest zainstalowanie pandas.
Wszystkie zmiany dokonane na zmiennych w powłoce interaktywnej po jej zamknięciu
zostają odrzucone, np. zmiana zmiennej int sam na sam + 100 itp.



Importowanie skrótów z innych edytorów np. notepad++, atom itd 
Extensions --> keymap i wyświetli się lista najpopularniejszych
keymapów z innych edytorów np.:
- Atom Keymap,
- Notepad++ keymap,
- Visual Studio keymap itd.




Odpalenie tylko części kodu:
Code Runner
Extensions --> code runner
by Jun Han
Zaznaczamy interesujący nas kod i klikamy PPM na zaznaczony kod
a następnie wybieramy 'Run Code'.
Warto dać: 
"code-runner.runInTerminal": true,
W pliku: settings.json, aby code runner mógł poradzić sobie z
takim czymś jak np. input(). w kodzie, gdy zachodzi potrzeba
interakcji z użytkownikiem w tym zaznaczonym fragmencie kodu.






Pakunek pandas.
Umożliwia podgląd danych w bardziej przyzwoitej formie:
'Show variable in data view'
Można wtedy filtrować dane itp.
Podglądać tak np. otrzymany JSON z backendu.
Wszystko w postaci tabelarycznej.
"""

pokoje = {49: 'Arkadiusz Włodarczyk', 69: 'Wioletta Włodarczyk'}

a = {'imie': 'Arkadiusz', 'nazwisko': 'Włodarczyk'} 
 

sam = 4
sampleNumber = 4

print(input("Podaj dane: "))
print(sam + 5)