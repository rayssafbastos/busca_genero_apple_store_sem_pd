import pandas as pd


data = pd.read_csv('files/AppleStore.csv')

genero = data['prime_genre']
genero_news = data.loc[(genero) == 'News']
quantidade_news = genero_news['rating_count_tot']
maior_valor_news = quantidade_news.max()
news_maior_quantidade_avaliacao = genero_news.loc[(quantidade_news) == maior_valor_news]
#print(news_maior_quantidade_avaliacao)


genero_music = data.loc[(genero) == 'Music']
genero_book = data.loc[(genero) == 'Book']
genero_book_music = pd.merge(genero_music, genero_book, how='outer')
quantidade_book_music = genero_book_music['rating_count_tot']
ordenar = genero_book_music.sort_values(by='rating_count_tot', ascending=False)
book_music_ordenado = ordenar.iloc[0:10]



op = pd.merge(book_music_ordenado, news_maior_quantidade_avaliacao, how='outer')
op.to_csv('Dados_apple_store.csv') # cria o csv

