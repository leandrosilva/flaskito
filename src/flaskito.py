from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Flaskito rulastonico running on a Java web container."
    
if __name__ == "__main__":
    app.run()