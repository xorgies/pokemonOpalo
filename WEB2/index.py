from flask import Flask, render_template
import sqlite3
from flask import g
import os
import json

app = Flask(__name__)

###################################################################
# rutas

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemonLista')
def lista_pokemon():
    dictPokemon= query_db('select id,name from Pokemon')

    return render_template('pokemon_lista.html', pokemon=dictPokemon)

@app.route('/pokemon/<int:pokemon_id>')
def pokemon(pokemon_id):
    dictPokemon= query_db('select * from datos_pokemon_view where id=?',[pokemon_id],one=True)
    dictHabilidades= query_db('select * from pokemon_habilidades_view where id=? order by tipo ASC',[pokemon_id])
    dictMovimientos= query_db('select * from pokemon_movimientos_view where id=? order by nivel_aprender ASC',[pokemon_id])
    dictEvoluciones=  query_db('select * from evoluciones_view where id=?',[pokemon_id])
    return render_template('pokemon.html', pokemon=dictPokemon, habilidades=dictHabilidades, movimientos=dictMovimientos, evoluciones=dictEvoluciones)

###################################################################
# DATABASE

DATABASE = 'WEB2/static/DB/database.sqlite3'

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

###################################################################
# Main

if __name__ == '__main__':
    # PRO
    #app.run(host='0.0.0.0')

    # Testing
    app.run(debug=True)