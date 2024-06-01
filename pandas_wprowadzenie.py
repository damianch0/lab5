import pandas as pd

# Wczytaj do DataFrame arkusza z nardzoinami dzieci w polsce dostpępny....
df = pd.read_excel('datasets/imiona.xlsx');
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df.Liczba[df.Liczba > 1000])
# Jak zrobić ingnoreCase ?
# tylko rekordy gdzie nadane imie jest takie jak Twoje
print(df.Imie[df.Imie == "DAMIAN"])
# sumę wszystkich dzieci urodzonych dzieci w całym danym okresie
print(df.agg({'Liczba': ['sum']}))
#  sumę dzieci urodzonych w latach 2000-2005
print(df.where(df.Rok >= 2000).where(df.Rok <= 2005).agg({'Liczba': ['sum']}))
# sumę urodzonych chłopców i dziewczynek
print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
# 2017 Ola
# 2017 Staś

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie

# Zadanie 3
ff = pd.read_csv('datasets/zamowienia.csv', header=0, sep=";", decimal=".")
# Listę unikalnych nazwisk przedawców
print(ff['Sprzedawca'].unique())
print(ff.sort_values(by='Utarg').head(5))


