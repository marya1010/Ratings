def mean_rating_date(df):
    for i in range(10):
        print(f'Средний рейтинг для {i+1}-го элемента по датам: \n',
              df[df[df.columns[0]] == i].groupby('date')['rating'].mean())


def mean_rating_week(df):
    df['year'] = df['date'].dt.year
    df['week'] = df['date'].dt.isocalendar().week
    for i in range(10):
        print(f'Средний рейтинг для {i+1}-го элемента по неделям: \n',
              df[df[df.columns[0]] == i].groupby(['year', 'week'])['rating'].mean())


def mean_rating_month(df):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    for i in range(10):
        print(f'Средний рейтинг для {i + 1}-го элемента по месяцам: \n',
              df[df[df.columns[0]] == i].groupby(['year', 'month'])['rating'].mean())


def mean_rating_gender(df):
    df.loc[df['user_gender'] == 0, 'user_gender'] = "male"
    df.loc[df['user_gender'] == 1, 'user_gender'] = "female"
    for i in range(10):
        print(f'Средний рейтинг для {i+1}-го элемента по полу: \n',
              df[df[df.columns[0]] == i].groupby('user_gender')['rating'].mean())


def mean_rating_age(df):
    for i in range(10):
        print(f'Средний рейтинг для {i+1}-го элемента по возрасту: \n',
              df[df[df.columns[0]] == i].groupby('user_age')['rating'].mean())


def mean_rating(df):
    print(f'Средний рейтинг для каждого элемента: \n',
          df.groupby(df.columns[0])['rating'].mean())
