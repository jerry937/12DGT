from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
@app.route('/')
def home ():
    return render_template('home.html', title = "ool Talo")




@app.route('/pizza/<int:id>')
def pizza(id):
  conn = sqlite3.connect('pizza.db')

  cursor = conn.cursor()
  cursor.execute("SELECT*FROM pizza WHERE id=?;",(1,))
  pizza = cursor.fetchone()
  conn.close()
  return render_template('pizza.html',pizza=pizza)
  

if __name__=="__main__":
     app.run(port=8080,host='127.0.0.0',debug=True)


