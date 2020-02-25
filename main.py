from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/jeffer")
def salvador():
    return "Hello, Jeffer"
 
@app.route("/home")
def home_html():
    return render_template("home_page.html")
   
if __name__ == "__main__":
    app.run(debug=True)
