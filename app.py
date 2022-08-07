from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def default():
    """
    The default static webpage
    """
    return render_template("index.html")
