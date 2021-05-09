from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('home.html',
    title = ("ool Talo"))


import sqlite3
@app.route('/pizza/<int:id>')
def pizza(id):
  conn = sqlite3.connect('pizza.db')

  cursor = conn.cursor()
  cursor.execute("SELECT*FROM pizza WHERE id=?;",(1,))
  pizza = cursor.fetchone()
  conn.close()
  return render_template('pizza.html',pizza=pizza)
  
  
  











@app.route('/')
def about():
  return render_template('home.html')

@app.route('/thing/<int:num>')
def thing (num):
  num2=num*num 
  return render_template('thing.html',
         num=num,num2=num2)
 
    


if __name__=="__main__":
     app.run(port=8080,host='0.0.0.0',debug=True)
     
     




 

  













     