from typing import no_type_check
from flask import Flask, redirect, render_template,request
app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
