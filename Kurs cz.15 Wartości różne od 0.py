a = 5
b = 7

# W warunkach wartości różne od zera są TRUE.
# Nie musi być to koniecznie 1
if (a < b):
    print("[a < b] Test")

if (125):
    print("[125] Test")

if (True):
    print("[True] Test")

if (-25):
    print("[-25] Test")


if (0):
    print("[0] Test")


if ('coś'):
    print("['coś'] Test")

# W Python'ie jest jeszcze coś takiego jak None
# Pustka, jak 0, symbolizuje FAŁSZ

if (None):
    print("[None] Test")
