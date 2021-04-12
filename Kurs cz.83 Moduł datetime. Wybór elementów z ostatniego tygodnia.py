import requests
import json
import webbrowser
from datetime import datetime, timedelta
"""
    Pytania z ostatniego tygodnia, generowanie daty według założeń.
    import datetime moduł
        from datetime import datetime, timedelta

    Dzięki importowaniu z zewnętrznego modułu elementów za pomocą
    from nie będzie trzeba pisać w programie całej formułki:
        datetime.datetime
        datetime.timedelta
    tylko od razu bezpośrednio:
        timedelta
        datetime
    DOCS:
        https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime


    Metoda today(): data teraz z czasem i sekundami
    timedelta <-- konstruktor klasy: różnica czasów, delta to inne słowo na różnica.
    Czas do odejmowania, do różnicy,
    np. od datetime.today(), jest to tak zrobione, że nie trzeba się martwić
    o coś, po prostu odejmujemy od today().
"""
'''
    time stamp - znak czasu
    1 stycznia 1970 - od tego momentu liczy się czas, ile sekund minęło od
    tej daty.
    timestamp jest zawsze liczony tak samo, można to przesłać gdzieś indziej, np.
    do innego środowiska programistycznego.
'''
"""
    int(searchDate.timestamp())
    Tydzień wcześniej (searchDate) zamienione na ogólny format czasu
    timestamp i rzutowany na int (same sekundy bez mikrosekund)
    Uzyskanie pytań z ostatniego tygodnia ze strony stackoverflow przy pomocy
    API i zapytania wraz z parametrami.
    Pytania z minimum 10 punktami.

    Można skrypt Python zapisać np. na pulpicie aby potem szybko otworzyć
    jakieś najbardziej potrzebne dla nas miejsca w Internecie w nowych
    zakładkach w domyślnej przeglądarce.
"""

print("datetime.today(): ")
print(datetime.today())
datetime.today()

print("timedelta(): ")
print(timedelta())

print("Tydzień: ")
print("timedelta(weeks=1): ")
print(timedelta(weeks=1))

print("timedelta(days=7): ")
print(timedelta(days=7))
print("==============================")
print("timedelta(days=2, hours=4): ")
print(timedelta(days=2, hours=4))


timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore
print("tydzień wcześniej od teraz: ")
print(searchDate)
print("Zamiana dowolnej daty na timestamp: ")
print(searchDate.timestamp())
print("Zamiana dowolnej daty na timestamp, bez mikrosekund, rzutowane na int: ")
print(int(searchDate.timestamp()))

params = {
    "site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": int(searchDate.timestamp()),
    "tagged": "python",
    "min": 10
}

r = requests.get("https://api.stackexchange.com/2.2/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])

