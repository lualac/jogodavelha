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
   g.db = psycopg2.connect("dbname=joguinho user=postgres password=ifpb host=127.0.0.1")

# Disconnect database
@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def index():
    return redirect(
    '/login'
    )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM Jogador where nome=%s and senha= %s;", (nome,senha))
        g.db.commit()
        data=cur.fetchall()
        cur.close()
        if len (data) > 0:
            session ['id'] = data[0]['id']
            return redirect( url_for('partidas') )
    return render_template(
        'login.html',
        title='Jogo da velha')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("INSERT INTO Jogador (nome,senha) VALUES (%s,%s);",(nome,senha,))
        cur.close()
        g.db.commit()
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM Jogador WHERE nome=%s and senha=%s ;",(nome,senha,))
        data = cur.fetchall()
        cur.close()
        if len (data) > 0:
            session ['id'] = data[0]['id']
            return redirect('/partidas')
    return render_template(
        'cadastro.html',
        title='Jogo da velha: cadastro')
#~~~~~~~~~~~~~~~
@app.route('/partidas')
def partidas():
    cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM partidas')
    data = cur.fetchall()
    cur.close()
    return render_template(
        'partidas.html',
        title='Jogo da velha',
        partidas=data)


@app.route('/velha/<pk>', methods = ['GET'])
def velha(pk):
    print 'opa', pk
    if pk == "new":
        cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("INSERT INTO partidas (jogador1) VALUES (%s)", (session['id'],))
        g.db.commit()
        cur.execute("SELECT idpartida from partidas where jogador1 = %s order by idpartida desc",(session['id'],))
        data = cur.fetchone()
        pk = data["idpartida"]
        cur.execute('SELECT * from  Partidas where idpartida=%s' ,(pk,))
        data = cur.fetchall()
        cur.close()
    return render_template(
        'jogo.html',
        title='Jogo da velha: Velha',
        partida=pk
        )

@app.route('/jogada', methods=['POST'])
def jogada ():
    pass
    #cur = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #Partidas =
    #cur.execute("UPDATE Partidas SET %s=%s where idpartida=%s" %(jogada,session['id'],Partidas))
    #g.db.commit()
    #cur.close()



@app.route('/espere')
def espere():
    return render_template(
    'espere.html'
    )

#~~~~~~~~~~~~~~~~~~
@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect( url_for('login') )
