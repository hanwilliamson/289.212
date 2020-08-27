from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)
STARSIGNSDB = 'starsigns.db'

def fetchMenu(con):
    signs = []
    cur = con.execute('SELECT name FROM signs')
    for row in cur:
        signs.append(list(row))

    return {'signs':signs}

@app.route('/')
def index():
    con = sqlite3.connect(STARSIGNSDB)
    menu = fetchMenu(con)
    con.close()

    return render_template('index.html',
                            footer= '© Hannah Williamson 2020',
                            signs=menu['signs']
                            )

@app.route('/order')
def order():
    con = sqlite3.connect(STARSIGNSDB)
    menu = fetchMenu(con)
    con.close()

    #cur = con.execute('SELECT name FROM signs')
    #for row in cur:
        #signs.append(list(row))

    return render_template('order.html',
                            footer= '© Hannah Williamson 2020',
                            signs=menu['signs']
                            )


@app.route('/result', methods=['POST'])
def result():
    # con = sqlite3.connect(STARSIGNSDB)
    # menu = fetchMenu(con)
    #
    # signs = []
    # cur = con.execute('SELECT name, image, ruling_planet, description, good_quality, bad_quality, lucky_number FROM signs')
    # for row in cur:
    #     signs.append(list(row))

    sign = {}


    for input in request.form:
        if input == '':
            return render_template('order.html',
                             footer= '© Hannah Williamson 2020',
                             signs=menu['signs']
                             )
        else:
            sign[input] = request.form[input]


    return render_template('result.html',
                            footer= '© Hannah Williamson 2020',
                            #signs=menu['signs']
                            )
