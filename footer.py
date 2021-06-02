from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def footer ():
    return render_template('footer.html', title = "ool Talo")

if __name__=="__main__":
     app.run(port=8081,host='127.0.0.1',debug=True)


