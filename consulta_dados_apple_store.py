import csv
from operator import itemgetter, attrgetter
from pprint import pprint
with open('files/AppleStore.csv', 'r') as content:
    data = csv.DictReader(content)
    rating_max_news = 0
    objeto_max_news = None
    objeto_book = []
    objeto_music = []
    for row in data:
        rating_count_tot = float(row['rating_count_tot'])

        if row['prime_genre'] == 'News':
            if rating_count_tot > rating_max_news:
                rating_max_news = rating_count_tot
                objeto_max_news = row


        if row['prime_genre'] == 'Book':
            objeto_book.append(row)
        

        if row['prime_genre'] == 'Music':
            objeto_music.append(row)

    objetos_max_music = sorted(objeto_music, key=lambda k: float(k['rating_count_tot']), reverse=True)[:10]
    objetos_max_book = sorted(objeto_book, key=lambda k: float(k['rating_count_tot']), reverse=True)[:10]
  

objeto_max_news_list = [objeto_max_news]
lista_para_csv = objeto_max_news_list + objetos_max_book + objetos_max_music

keys = []
dicionario = lista_para_csv[0]

for k in dicionario:
    keys.append(k)





with open('consulta_apple_store.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for row in lista_para_csv:
        writer.writerow(row.values())
        



 