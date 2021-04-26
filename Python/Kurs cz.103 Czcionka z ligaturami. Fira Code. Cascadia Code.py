"""
    Czcionka dla programistów, do pobrania:
    Cascadia Code albo Fira Code


    Fira Code:
    Np <= zamieni na ligaturę, pojedynczy symbol.
    Połączenie dwóch lub więcej znaków w jeden cały.

    Tak samo jak dla np.:
    >=
    <=
    ==
    !=
    =>
    ->
    <-

    Ułatwia czytanie zmiennych:
    Il1sample


    https://github.com/microsoft/cascadia-code
    https://github.com/tonsky/FiraCode

    Ściągnięcie Cascadia Code jako zip z repo github
    Wypakowanie
    Ściągnięcie Fira Code jako zip z repo github
    Wypakowanie   

    Wchodzimy do lokalizacji:
    ...:\...\Downloads\FiraCode-master\FiraCode-master\distr\ttf
    Zaznaczamy wszystkie 6 pozycji, PPM i install.
    Gotowe
    Następnie instalacja Cascadia Code:
    ...:\...\Downloads\cascadia-code-main\cascadia-code-main\sources\vtt_data
    PPM i install
    Gotowe
    =========================================================

    Używanie tych fontów w VSC:
    Settings --> font --> Editor: Font Family
    Lub chwilowo w:
    settings.json
    "editor.fontFamily": "Consolas, 'Courier New', monospace",
    Rodzina fontów do użycia w edytorze,
    wypisane w kolejności chodzi o to, że jak zostanie w komputerze
    znaleziona czcionka Consolas, to ona będzie używana, w następnej
    kolejności byłaby używana, gdyby nie było Consolas, Courier New, 
    a na samym końcu do sprawdzenia idzie monospace.

    Zmiana na:
    "editor.fontFamily": "'Fira Code', Consolas, 'Courier New', monospace",
    "editor.fontFamily": "'Cascadia Code', 'Fira Code', Consolas, 'Courier New', monospace",

    ==========================================================

    Ligatury też trzeba oddzielnie 'uruchomić'.
    "editor.fontLigatures": true,
    Ligatury też można ustawić globalnie dla całego edytora w:
    settings --> font --> Editor: Font Ligatures
"""