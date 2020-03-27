import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Student sdb</h1>
<p>This is a sdb that includes information related to students</p>'''


@app.route('/api/v1/resources/sdb/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('sdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_sdb = cur.execute('SELECT * FROM sdb;').fetchall()

    return jsonify(all_sdb)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/sdb', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    f_name = query_parameters.get('f_name')
    l_name = query_parameters.get('l_name')

    query = "SELECT * FROM sdb WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if f_name:
        query += ' f_name=? AND'
        to_filter.append(f_name)
    if l_name:
        query += ' l_name=? AND'
        to_filter.append(l_name)
    if not (id or f_name or l_name):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('sdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()