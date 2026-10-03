from flask import Flask , render_template, url_for, redirect, request

app = Flask(__name__, template_folder='templates')
movies = [
  {"id":1,"title":"Гра в кальмара","year":2023,"genre":"Бойовик","discription":"Гра про багатих і бідних"},
  {"id":2,"title":"Вижити в зграї","year":2019,"genre":"Драма","discription":"Група людей бореться за життя у світі нерівності"},
  {"id":3,"title":"Хмарочос справедливості","year":2021,"genre":"Трилер","discription":"Охоронець з нетрів кидає виклик багатим"},
  {"id":4,"title":"На межі прірви","year":2018,"genre":"Кримінал","discription":"Брати з бідного району йдуть на крайні заходи"},
  {"id":5,"title":"Заможні сни","year":2020,"genre":"Драма","discription":"Життя еліти у світі злиднів"},
  {"id":6,"title":"Повстання армії тіней","year":2022,"genre":"Екшн","discription":"Нижчі класи готують переворот"},
  {"id":7,"title":"Револьвер між нами","year":2017,"genre":"Трилер","discription":"Мисливець за нагородами між двома світами"},
  {"id":8,"title":"Стежка від нерівності","year":2016,"genre":"Пригоди","discription":"Боротьба за справедливість у жорстокому світі"},
  {"id":9,"title":"Клан висот","year":2024,"genre":"Драма","discription":"Еліта на верхівці, злидні — внизу"},
  {"id":10,"title":"Межа глибини","year":2015,"genre":"Трилер","discription":"Шахтар викриває змову корпорацій"},
  {"id":11,"title":"Біла маска","year":2013,"genre":"Кримінал","discription":"Месник у масці захищає своє місто"},
  {"id":12,"title":"Кров за закони","year":2014,"genre":"Бойовик","discription":"Сутичка між охоронцями багатіїв та владою"},
  {"id":13,"title":"Злотий кайдан","year":2020,"genre":"Політичний трилер","discription":"Багаті тримають у кайданах цілий світ"},
  {"id":14,"title":"Привілеї і порох","year":2022,"genre":"Військовий","discription":"Солдати — розмінна монета в руках багатих"},
  {"id":15,"title":"Тінь у золоті","year":2018,"genre":"Драма","discription":"Зрада в колах еліти"},
  {"id":16,"title":"Останній рівень","year":2021,"genre":"Фантастика","discription":"Боротьба за виживання в ієрархічному суспільстві"},
  {"id":17,"title":"Вірні своїм","year":2019,"genre":"Кримінал","discription":"Банда з нетрів шукає справедливості"},
  {"id":18,"title":"Збір колючого дроту","year":2017,"genre":"Воєнна драма","discription":"Війна відкриває очі на класову нерівність"},
  {"id":19,"title":"Політ над багатством","year":2023,"genre":"Фантастика","discription":"Літаючі міста для еліти — злидні внизу"},
  {"id":20,"title":"Протистояння тіней","year":2016,"genre":"Трилер","discription":"Боротьба агентів за правду в системі"},
  {"id":21,"title":"Замкнені в золотих клітках","year":2014,"genre":"Драма","discription":"Багаті тримають інших у неволі"},
  {"id":22,"title":"Унир між рівнями","year":2022,"genre":"Фантастика","discription":"Кожен рівень — нове пекло"},
  {"id":23,"title":"Без прикрас","year":2021,"genre":"Драма","discription":"Жорстка реальність життя без ілюзій"},
  {"id":24,"title":"Гра капіталу","year":2018,"genre":"Політичний трилер","discription":"Бізнесмени використовують бідних для зиску"},
  {"id":25,"title":"Колиска влади","year":2020,"genre":"Драма","discription":"Лідер з нетрів прагне змінити систему"},
  {"id":26,"title":"Поріг надії","year":2015,"genre":"Драма","discription":"Боротьба за краще майбутнє"},
  {"id":27,"title":"Золотий ланцюг","year":2017,"genre":"Кримінал","discription":"Корупція серед багатіїв"},
  {"id":28,"title":"Голоси з підвалу","year":2019,"genre":"Драма","discription":"Ті, кого не чують, піднімаються"},
  {"id":29,"title":"Кров і прести","year":2021,"genre":"Бойовик","discription":"Війна гільдій за владу"},
  {"id":30,"title":"Шлях з попелу","year":2022,"genre":"Драма","discription":"Історія піднесення через біль і втрати"}
]

@app.route('/')
def index():
    return render_template("index.html",movies = movies)

@app.route('/movie/<int:movie_id>/')
def movie_detail(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id),None)
    if movie:
        return render_template("movie.html",movie = movie)
    return """<h1>Фільм не найдено</h1>""", 404

@app.route("/add",methods = ['GET', "POST"])
def add_movie():
    if request.method == "POST":
        new_id = max([movie['id'] for movie in movies]) + 1
        new_movie = {
            "id":new_id,
            "title":request.form['title'],
            "year":int(request.form['year']),
            "genre":request.form['genre'],
            "description":request.form['description']
        }
        movies.append(new_movie)
        return render_template(url_for("index"))
    return render_template('add.html')





@app.route('/genres/')
def genres():
    uni_genres = sorted(set(movie['genre'] for movie in movies))
    return render_template('genres.html', genres=uni_genres)





@app.route('/genre/<genre_name>')
def genre_movie(genre_name):
    filtered = [m for m in movies if m['genre'].lower() == genre_name.lower()]
    return render_template('gener_movie.html',genre = genre_name,movie = filtered)

@app.route('/search')
def search():
    result = []
    query = ""
    if request.method == "POST":
        query = request.form['query'].lower()
        result = [m for m in movies if query in m['title'].lower()]
    return render_template('search.html',result = result, query = query)

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
    