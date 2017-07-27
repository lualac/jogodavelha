# coding=utf-8

from flask import g, session, render_template, request, redirect, url_for

from app import app

import psycopg2, psycopg2.extras

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Connect database
# g = http://flask.pocoo.org/docs/0.12/api/#flask.g
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.before_request
def before_request():
   g.db = psycopg2.connect("dbname=velha user=postgres password=ifpb host=127.0.0.1")

# Disconnect database
@app.teardown_request
def teardown_request(exception):
    g.db.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#def artists():

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur.execute("SELECT * FROM artista;")
    #data = cur.fetchall()
    #cur.close()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #return render_template(
        #'artists/list.html',
        #title='MovieApp: Artistas',
        #data=data)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#@app.route('/movies')
#def movies():
    #return render_template(
        #'movies/list.html',
        #title='MovieApp: Filmes')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM Jogador where email=%s and senha= %s;" % (email,senha))
        data = cur.fetchall()
        cur.close()
        if len (data) > 0:
            session['email'] = email
            session ['id'] = data[0]['id']
            return redirect( url_for('partidas') )
    return render_template(
        'login.html',
        title='MovieApp: Login')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("INSERT INTO Jogador (nome,email,senha) VALUES ('%s','%s','%s');" (nome,email,senha))
        data = cur.fetchall()
        cur.close()
        if len (data) > 0:
            session['email'] = email
            session ['id'] = data[0]['id']
            return redirect( url_for('partidas') )
    return render_template(
        'cadastro.html',
        title='MovieApp: cadastro')
#~~~~~~~~~~~~~~~
@app.route('/partidas')
def partidas():
    cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM partidas')
    data = cur.fetchall()
    cur.close()
    return render_template(
        'partidas.html',
        title='MovieApp: Jogar',
        partidas=data)

#~~~~~~~~~~~~~~~~~~
#@app.route('/logout')
#def logout():
    #session.pop('email', None)
    #return redirect( url_for('artists') )

# @app.route('/')
# @app.route('/index')
# def index():
#     # return 'Hello world'
#
#     # return render_template('index_.html')
#
#     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute("SELECT * FROM foto;")
#     photos = cur.fetchall()
#     cur.close()
#     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#     user = {'nickname': 'Jovens', 'notas': [100, 90, 50], 'photos': photos}
#     return render_template('base.html',
#                            title='Home',
#                            user=user)
#
# @app.route('/usuarios')
# def users():
#     users = [ 'Gustavo', 'Soares', 'Vieira' ]
#     return render_template('users.html', users=users)
#
# @app.route('/usuarios/<pk>/', methods=['GET',])
# def user_form(pk):
#     return render_template('user.html', pk=pk)
#
# @app.route('/usuarios/<pk>/', methods=['POST',])
# def user(pk):
#     name = request.form['nome']
#     return render_template('user.html', pk=pk, name=name)
