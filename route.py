
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
 
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/") 
def hello(): 
    #return "Hello, Welcome to GeeksForGeeks"
    return render_template('first.html')

@app.route('/aboutus')
def index():
    #return "Meet the team!"
    return render_template('aboutus.html')
    
@app.route("/Luke") 
def Luke(): 
    return "Homepage of GeeksForGeeks"
    #return render_template('luke.html')
@app.route("/store")
def store(): 
    return render_template('store.html')

if __name__ == "__main__": 
    app.run(debug=True) 

