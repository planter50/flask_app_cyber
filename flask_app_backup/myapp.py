
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
 
app = Flask(__name__) 
  
# Pass the required route to the decorator. 
@app.route("/contact") 
def contact1(): 
    #return "Hello, welcome to cyberebels! Checkout https:cyberebels.com/aboutus to see more"
    return render_template('contact.html')

@app.route('/aboutus')
def index():
    #return "Meet the team!"
    return render_template('aboutus.html')
    
@app.route("/") 
def mainpage1(): 
    #return "Homepage of GeeksForGeeks"
    return render_template('mainpage.html')
@app.route("/services")
def services1(): 
    return render_template('services.html')
    #return "work in progress"
if __name__ == "__main__": 
    app.run(debug=True) 

