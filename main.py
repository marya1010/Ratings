from functions import *
import pandas as pd


d = {1: 'movies_csv.csv', 2: 'books_csv.csv', 3: 'books_csv.csv'}

while True:
    print('Если хотите завершить работу, введите 0.')
    print('Выберите, для каких данных вы хотите получить статистику '
          '(1 - фильмы, 2 - книги, 3 - музыка): ')
    file = int(input())
    if file == 0:
        print('Программа завершена.')
        break
    if file not in [1, 2, 3]:
        print('Ошибка ввода данных, начните заново.')
        continue
    print('Выберите, по какому признаку вы хотите сортиовать данные (1 - день, '
          '2 - неделя, 3 - месяц, 4 - пол пользователя, 5 - возраст пользователя, 6 - общий рейтинг): ')
    sort = int(input())
    if sort not in [1, 2, 3, 4, 5, 6]:
        print('Ошибка ввода данных, начните заново.')
        continue
    df = pd.read_csv(d[file])
    df['date'] = pd.to_datetime(df['date'])
    if sort == 1:
        mean_rating_date(df)
    elif sort == 2:
        mean_rating_week(df)
    elif sort == 3:
        mean_rating_month(df)
    elif sort == 4:
        mean_rating_gender(df)
    elif sort == 5:
        mean_rating_age(df)
    elif sort == 6:
        mean_rating(df)
