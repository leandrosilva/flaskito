from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Flaskito rulastonico potentially running on a Java web container. Could it be Jetty, right?"
    
if __name__ == "__main__":
    app.run()