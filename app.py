import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    #do whatevr here...
    return "Hello Heruko"