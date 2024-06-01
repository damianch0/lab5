import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import numpy as np
#
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# #
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# print(df.dtypes)
# df.to_csv('plik.csv', index=False)
#
# print(s['c'])
# print(s.c)
# print(df[0:1])
# print("")
# print(df["Populacja"])
# print(df.iloc[0, 0])
# print(df.loc[0, "Kraj"])
# print(df.at[0, "Kraj"])
# print('Kraj: ' + df.Kraj)
# print(df.sample())
# print()
# print(df.sample(2))
# print()
# print(df.sample(frac=0.5))
# print()
# print(df.sample())
# print()
# print(df.sample(n=10, replace=True))
# print()
# print(df.head())
# print()
# print(df.head(2))
# print()
# print(df.tail(1))
# print()
# print(df.describe())
# print()
# print(df.T)
#
# print(s[(s > 9)])
# print(s.where(s > 10))
# print(s.where(s > 10, 'za duzo'))
# seria = s.copy()
# seria.where(seria > 10, 'za duzo', inplace=True)
# print("#######")
# print(seria)
#
# print(s[~(s > 10)])
# print(s[(s < 13) & (s > 8)])
#
# print(df[(df.Populacja > 100000) & (df.index.isin(([0, 2])))])
#
# print("######")
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))
#
# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)
#
#
# df.loc[3] = 'dodane'
# print(df)
# df.loc[4] = ['Polska', 'Warszawa', '38675467']
# print(df)
#
# new_df = df.drop([3])
# print(new_df)
#
# df.drop([3], inplace=True)
# print(df)
#
# # df.drop('Kraj', axis=1, inplace=True)
df['kontynent'] = ['Europa', 'Azja', 'Aeryka południowa']
#
# print(df)
# print(df.sort_values(by='Kraj'))
# grouped = df.groupby(['kontynent'])
# print(grouped.get_group('Europa'))
# print((df.groupby(['kontynent']).agg({'Populacja': ['sum']})))
# print((df.groupby(['kontynent']).agg('Populacja').sum()))
#


# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()
# #
# grupa = df.groupby(['kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='Kontytent', ylabel='Mld', rot=0, legend=True, title='Populacja z podziałem na kontytenty')
# wykres = grupa.plot.bar()
# wykres.set_ylabel("Mld")
# wykres.set_xlabel("kontytent")
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title("Populacja z podziałem na kontytenty")
# # plt.savefig('wykres.png')
# # plt.xticks(rotation=1)
# plt.show()
#
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
#
# print(df)
# grupa = (df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), colors=['red', 'green'])
#
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts, columns=['wartości'])
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()
