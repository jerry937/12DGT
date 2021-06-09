from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home ():
    return render_template('home.html',
    title = ("ool Talo"))


@app.route('/all_cake')
def all_cake ():
    return render_template('/all_cake.html')
   






if __name__=="__main__":
     app.run(port=8080 ,host='127.0.0.1',debug=True)